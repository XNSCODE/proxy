import os
import sys
import re
import time
import random
import requests as ses

class Main:
	def __init__(self):
		self.url = "https://free-proxy-list.net/"
		proxies = []
		os.system("clear")
		print(" ____________________ ________  ____  ________.___.\n \______   \______   \\_____   \ \   \/  /\__  |   |\n  |     ___/|       _/ /   |   \ \     /  /   |   |\n  |    |    |    |   \/    |    \/     \  \____   |\n  |____|    |____|_  /\_______  /___/\  \ / ______|\n                   \/         \/      \_/ \/       \n        [ GET PROXY FROM FREE-PROXYLIST ]\n")
		prxy = ses.get(self.url).text
		proxy = re.findall(r"<tr><td>(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})</td><td>(\d+?)</td>", prxy)
		for x in proxy:
			proxies.append(":".join(x))
		try:tanya_total = int(input(" [?] masukan jumlah (cth: 10): "))
		except:tanya_total = 1
		print(" [!] harap tunggu sebentar...\n")
		time.sleep(1.5) 
		for total in range(tanya_total):
			total +=1
			prx = random.choice(proxies)
			print(" [+] proxy %s : %s"%(total, prx))
		ask = input("\n [?] ingin dapatkan proxy lagi? [Y/n]: ")
		if ask in ["Y", "y"]:
			Main()
		else:
			exit(" [!] keluar... ")

try:
	Main()
except Exception as e:
	exit(str(e))
