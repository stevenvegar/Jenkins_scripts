import argparse
import base64
import json
import random
import requests
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def parse_args():
	parser = argparse.ArgumentParser(description='This script can enumerate 26 different URLs and check if the user can access them.')
	parser.add_argument('-w', '--website', type=str, required=True, help='Required. Jenkins website URL')
	parser.add_argument('-wp', '--webport', type=int, help='Jenkins website port (default: 8080)')
	parser.add_argument('-u','--username', type=str, help='Jenkins username (default: anonymous)')
	parser.add_argument('-p','--password', type=str, help='Jenkins password (default: '')')
	parser.add_argument('--local_proxy', action='store_true', help="Enable local proxy (default: {'http': 'http://127.0.0.1:8080'})")
	return parser.parse_args()


def main():
	args = parse_args()
	WEB_URL = args.website if 'http' in args.website else 'http://' + args.website
	WEB_PORT = args.webport if args.webport else 8080
	WEBSITE = str(WEB_URL) + ':' + str(WEB_PORT)
	USERNAME = args.username if args.username else "anonymous"
	PASSWORD = args.password if args.password else ""
	PROXIES = {'http': 'http://127.0.0.1:8080'} if args.local_proxy else None

	if USERNAME != "anonymous":
		bearer = str(base64.b64encode(bytes(USERNAME + ":" + PASSWORD, "utf-8")), encoding='ascii')
		headers = {"Authorization": "Basic " + bearer}
	else:
		headers = None

	try:
		r = requests.get(WEBSITE, headers=headers, proxies=PROXIES)
		#Checking connection to Jenkins server
		print("[>] Connecting to Jenkins server", end='', flush=True); [print('.', end='', flush=True) or time.sleep(0.5) for _ in range(5)]; print()
		#Server information based on response headers
		print ("[+] Server version: " + r.headers['Server'])
		print ("[+] Jenkins version: " + r.headers['X-Jenkins'])
		print ("[+] Hudson version: " + r.headers['X-Hudson'])
		print ("[ ] ...")
		if r.status_code == 200:
			print (f"[>] Using {USERNAME} for authentication...")
			print ("[+] 1. Can the user view Jenkins dashboard? YES !")
			print (f"   [>] {WEBSITE}/")
		elif r.status_code == 403:
			print (f"[>] Using {USERNAME} for authentication...")
			print ("[-] 1. Can the user Jenkins dashboard? NO !")
	except:
		if r.status_code == 401:
			print (f"[>] Using {USERNAME} for authentication...")
			print ("[-] Error: Username and/or password are incorrect. Check credentials.")
			exit()
		print ("[-] Error: Can not connect to Jenkins server. Check URL and port.")
		exit()

	try:
		s = requests.get(WEBSITE + "/crumbIssuer/api/json", headers=headers, proxies=PROXIES)
		if s.status_code == 200:
			print ("[+] 2. Can the user request a new \"Crumb Token\"? YES !")
			jcrumb = s.json()["crumb"]
			print (f"   [>] Jenkins-Crumb: {jcrumb}")
		elif s.status_code == 403:
			jcrumb = "null"
			print ("[-] 2. Can the user request a new \"Crumb Token\"? NO !")
	except:
		print ("[-] Error: Can not connect to Jenkins server. Check URL and port.")
		exit()

	try:
		s = requests.get(WEBSITE + "/newJob", headers=headers, proxies=PROXIES)
		if s.status_code == 200:
			print ("[+] 3. Can the user create a New Job? YES !")
			print (f"   [>] {WEBSITE}/newJob")
		elif s.status_code == 403:
			print ("[-] 3. Can the user create a New Job? NO !")
	except:
		print ("[-] Error: Can not connect to Jenkins server. Check URL and port.")
		exit()

	try:
		s = requests.get(WEBSITE + "/view/all/", headers=headers, proxies=PROXIES)
		if s.status_code == 200:
			print ("[+] 4. Can the user view Existing Jobs? YES !")
			print (f"   [>] {WEBSITE}/view/all/")
		elif s.status_code == 403:
			print ("[-] 4. Can the user view Existing Jobs? NO !")
	except:
		print ("[-] Error: Can not connect to Jenkins server. Check URL and port.")
		exit()

	try:
		s = requests.get(WEBSITE + "/view/all/builds", headers=headers, proxies=PROXIES)
		if s.status_code == 200:
			print ("[+] 5. Can the user view Build History? YES !")
			print (f"   [>] {WEBSITE}/view/all/builds")
		elif s.status_code == 403:
			print ("[-] 5. Can the user view Build History? NO !")
	except:
		print ("[-] Error: Can not connect to Jenkins server. Check URL and port.")
		exit()

	try:
		s = requests.get(WEBSITE + "/script", headers=headers, proxies=PROXIES)
		if s.status_code == 200:
			print ("[+] 6. Can the user access to Script Console? YES !")
			print (f"   [>] {WEBSITE}/script")
		elif s.status_code == 403:
			print ("[-] 6. Can the user access to Script Console? NO !")
	except:
		print ("[-] Error: Can not connect to Jenkins server. Check URL and port.")
		exit()

	try:
		s = requests.get(WEBSITE + "/jnlpJars/jenkins-cli.jar", headers=headers, proxies=PROXIES)
		if s.status_code == 200:
			print ("[+] 7. Can the user Download jenkins-cli.jar? YES !")
			print (f"   [>] {WEBSITE}/jnlpJars/jenkins-cli.jar")
		elif s.status_code == 403:
			print ("[-] 7. Can the user Download jenkins-cli.jar? NO !")
	except:
		print ("[-] Error: Can not connect to Jenkins server. Check URL and port.")
		exit()

	try:
		s = requests.get(WEBSITE + "/computer/", headers=headers, proxies=PROXIES)
		if s.status_code == 200:
			print ("[+] 8. Can the user view Node Information? YES !")
			print (f"   [>] {WEBSITE}/computer/")
		elif s.status_code == 403:
			print ("[-] 8. Can the user view Node Information? NO !")
	except:
		print ("[-] Error: Can not connect to Jenkins server. Check URL and port.")
		exit()

	try:
		s = requests.get(WEBSITE + "/load-statistics", headers=headers, proxies=PROXIES)
		if s.status_code == 200:
			print ("[+] 9. Can the user view Load Statistics? YES !")
			print (f"   [>] {WEBSITE}/load-statistics")
		elif s.status_code == 403:
			print ("[-] 9. Can the user view Load Statistics? NO !")
	except:
		print ("[-] Error: Can not connect to Jenkins server. Check URL and port.")
		exit()

	try:
		s = requests.get(WEBSITE + "/env-vars.html/", headers=headers, proxies=PROXIES)
		if s.status_code == 200:
			print ("[+] 10. Can the user view Enviroment Variables? YES !")
			print (f"   [>] {WEBSITE}/env-vars.html/")
		elif s.status_code == 403:
			print ("[-] 10. Can the user view Enviroment Variables? NO !")
	except:
		print ("[-] Error: Can not connect to Jenkins server. Check URL and port.")
		exit()

	try:
		s = requests.get(WEBSITE + "/instance-identity/", headers=headers, proxies=PROXIES)
		if s.status_code == 200:
			print ("[+] 11. Can the user view Instance Identity? YES !")
			print (f"   [>] {WEBSITE}/instance-identity/")
		elif s.status_code == 403:
			print ("[-] 11. Can the user view Instance Identity? NO !")
	except:
		print ("[-] Error: Can not connect to Jenkins server. Check URL and port.")
		exit()

	try:
		s = requests.get(WEBSITE + "/administrativeMonitor/OldData/", headers=headers, proxies=PROXIES)
		if s.status_code == 200:
			print ("[+] 12. Can the user view Jenkins Old Data? YES !")
			print (f"   [>] {WEBSITE}/administrativeMonitor/OldData/")
		elif s.status_code == 403:
			print ("[-] 12. Can the user view Jenkins Old Data? NO !")
	except:
		print ("[-] Error: Can not connect to Jenkins server. Check URL and port.")
		exit()

	try:
		s = requests.get(WEBSITE + "/manage", headers=headers, proxies=PROXIES)
		if s.status_code == 200:
			print ("[+] 13. Can the user access Admin panel? YES !")
			print (f"   [>] {WEBSITE}/manage")
		elif s.status_code == 403:
			print ("[-] 13. Can the user access Admin panel? NO !")
	except:
		print ("[-] Error: Can not connect to Jenkins server. Check URL and port.")
		exit()

	try:
		s = requests.get(WEBSITE + "/configfiles/", headers=headers, proxies=PROXIES)
		if s.status_code == 200:
			print ("[+] 14. Can the user view Config File Management? YES !")
			print (f"   [>] {WEBSITE}/configfiles/")
		elif s.status_code == 403:
			print ("[-] 14. Can the user view Config File Management? NO !")
	except:
		print ("[-] Error: Can not connect to Jenkins server. Check URL and port.")
		exit()

	try:
		s = requests.get(WEBSITE + "/log/", headers=headers, proxies=PROXIES)
		if s.status_code == 200:
			print ("[+] 15. Can the user view logs? YES !")
			print (f"   [>] {WEBSITE}/log/")
		elif s.status_code == 403:
			print ("[-] 15. Can the user view logs? NO !")
	except:
		print ("[-] Error: Can not connect to Jenkins server. Check URL and port.")
		exit()

	try:
		s = requests.get(WEBSITE + "/pluginManager/installed", headers=headers, proxies=PROXIES)
		if s.status_code == 200:
			print ("[+] 16. Can the user view Installed Plugins? YES !")
			print (f"   [>] {WEBSITE}/pluginManager/installed")
		elif s.status_code == 403:
			print ("[-] 16. Can the user view Installed Plugins? NO !")
	except:
		print ("[-] Error: Can not connect to Jenkins server. Check URL and port.")
		exit()

	try:
		s = requests.get(WEBSITE + "/configureSecurity/", headers=headers, proxies=PROXIES)
		if s.status_code == 200:
			print ("[+] 17. Can the user Configure Global Security? YES !")
			print (f"   [>] {WEBSITE}/configureSecurity/")
		elif s.status_code == 403:
			print ("[-] 17. Can the user Configure Global Security? NO !")
	except:
		print ("[-] Error: Can not connect to Jenkins server. Check URL and port.")
		exit()

	try:
		s = requests.get(WEBSITE + "/configureTools/", headers=headers, proxies=PROXIES)
		if s.status_code == 200:
			print ("[+] 18. Can the user view Global Tool Configuration? YES !")
			print (f"   [>] {WEBSITE}/configureTools/")
		elif s.status_code == 403:
			print ("[-] 18. Can the user view Global Tool Configuration? NO !")
	except:
		print ("[-] Error: Can not connect to Jenkins server. Check URL and port.")
		exit()

	try:
		s = requests.get(WEBSITE + "/credentials/", headers=headers, proxies=PROXIES)
		if s.status_code == 200:
			print ("[+] 19. Can the user view Credentials? YES !")
			print (f"   [>] {WEBSITE}/credentials/")
		elif s.status_code == 403:
			print ("[-] 19. Can the user view Credentials? NO !")
	except:
		print ("[-] Error: Can not connect to Jenkins server. Check URL and port.")
		exit()

	try:
		s = requests.get(WEBSITE + "/credentials/store/system/domain/_/", headers=headers, proxies=PROXIES)
		if s.status_code == 200:
			print ("[+] 20. Can the user view Global credentials (unrestricted)? YES !")
			print (f"   [>] {WEBSITE}/credentials/store/system/domain/_/")
		elif s.status_code == 403:
			print ("[-] 20. Can the user view Global credentials (unrestricted)? NO !")
	except:
		print ("[-] Error: Can not connect to Jenkins server. Check URL and port.")
		exit()

	try:
		random_name = "user_" + ''.join(random.choice('0123456789') for i in range(6))
		data = {
			"username": random_name,
			"password1": random_name,
			"password2": random_name,
			"fullname": random_name,
			"email": random_name + "@mail.com",
			"Jenkins-Crumb": jcrumb,
			"Submit": "Create account"}		
		s = requests.post(WEBSITE + "/securityRealm/createAccount", data=data, headers=headers, proxies=PROXIES)
		if s.status_code == 200:
			print ("[+] 21. Can the user SignUp new users? YES !")
			print (f"   [>] {WEBSITE}/securityRealm/user/{random_name}/")
		elif s.status_code == 401:
			print ("[-] 21. Can the user SignUp new users? NO !")
			print ("   [x] Signing Up new users is disabled")			
		elif s.status_code == 403:
			print ("[-] 21. Can the user SignUp new users? NO !")
		elif s.status_code == 404:
			print ("[-] 21. Can the user SignUp new users? NO !")
			print ("   [x] Local authentication disabled")
	except:
		print ("[-] Error: Can not connect to Jenkins server. Check URL and port.")
		exit()

	try:
		random_name = "user_" + ''.join(random.choice('0123456789') for i in range(6))
		data = {
			"username": random_name,
			"password1": random_name,
			"password2": random_name,
			"fullname": random_name,
			"email": random_name + "@mail.com",
			"Jenkins-Crumb": jcrumb,
			"Submit": "Create User"}
		s = requests.post(WEBSITE + "/securityRealm/createAccountByAdmin", data=data, headers=headers, proxies=PROXIES, allow_redirects=False)
		if s.status_code == 302:
			print ("[+] 22. Can the user add new Admin users? YES !")
			print (f"   [>] {WEBSITE}/securityRealm/user/{random_name}/")
		elif s.status_code == 403:
			print ("[-] 22. Can the user add new Admin users? NO !")
		elif s.status_code == 404:
			print ("[-] 22. Can the user add new Admin users? NO !")
			print ("   [x] Local authentication disabled")
	except:
		print ("[-] Error: Can not connect to Jenkins server. Check URL and port.")
		exit()

	try:
		s = requests.get(WEBSITE + "/asynchPeople/", headers=headers, proxies=PROXIES)
		if s.status_code == 200:
			print ("[+] 23. Can the user view local user list? YES !")
			print (f"   [>] {WEBSITE}/asynchPeople/")
		elif s.status_code == 403:
			print ("[-] 23. Can the user view local user list? NO !")
	except:
		print ("[-] Error: Can not connect to Jenkins server. Check URL and port.")
		exit()

	try:
		s = requests.get(WEBSITE + "/securityRealm/", headers=headers, proxies=PROXIES)
		if s.status_code == 200:
			print ("[+] 24. Can the user view Jenkins own user database? YES !")
			print (f"   [>] {WEBSITE}/securityRealm/")
		elif s.status_code == 403:
			print ("[-] 24. Can the user view Jenkins own user database? NO !")
		elif s.status_code == 404:
			print ("[-] 24. Can the user view Jenkins own user database? NO !")
			print ("   [x] Local authentication disabled")
	except:
		print ("[-] Error: Can not connect to Jenkins server. Check URL and port.")
		exit()

	try:
		s = requests.get(WEBSITE + "/ad-health/", headers=headers, proxies=PROXIES)
		if s.status_code == 200:
			print ("[+] 25. Can the user view Active Directory health? YES !")
			print (f"   [>] {WEBSITE}/ad-health/")
		elif s.status_code == 403:
			print ("[-] 25. Can the user view Active Directory health? NO !")
		elif s.status_code == 404:
			print ("[-] 25. Can the user view Active Directory health? NO !")
			print ("   [x] AD plugin not installed")
	except:
		print ("[-] Error: Can not connect to Jenkins server. Check URL and port.")
		exit()

	try:
		s = requests.get(WEBSITE + "/whoAmI/", headers=headers, proxies=PROXIES)
		if s.status_code == 200:
			print ("[+] 26. Can the user view current user information? YES !")
			print (f"   [>] {WEBSITE}/whoAmI/")
		elif s.status_code == 403:
			print ("[-] 26. Can the user view current user information? NO !")
	except:
		print ("[-] Error: Can not connect to Jenkins server. Check URL and port.")
		exit()


if __name__ == "__main__":
	main()
