# '/usr/bin/python3.11'
# -*- coding: utf-8 -*-
# python required 3.3.2 or higher Subdomain_finder Script version1
# developed by: Red Mahdi
# only for legal purpose


# ---------------Import Modules---------------
import os
import requests
from requests.exceptions import ConnectionError
from time import sleep
import pyfiglet
from wordlists import wordlist as lst

# ---Program Stabilization---
os.system('')

# ----Define Fonts----
class fonts:
    BIG = 'big'
    LARRY3D = 'larry3d'

# ----Define Colors----
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    
# --------------------Making-a-Logo--------------------
logoName = "SUBSFINDER"
print(bcolors.WARNING, pyfiglet.figlet_format(logoName, font=fonts.BIG),bcolors.ENDC)

# ---------------Start Program---------------
url = input("Enter url: ")
print("Please wait, The program is receiving the wordlist...")
sleep(5)
print("")
print("-" * 11 + 'Program Started' + "-" * 11)
print(' Hostname   |    Code')
print("")

# ---Define-strat-Function---
def check():
    for i in lst:
        
        # --Handle-a-ConnectionError(Code:403)--
        try:

            r = requests.get('http://' + i[::] + url)
            code = r.status_code
            if code == 200:
                print(bcolors.OKGREEN, i[::] + url + ':', code, bcolors.ENDC)
            else:
                pass

        except ConnectionError as e:
            r = "No response"
             
check()

# ---------------Finish Program---------------
print("")
print("-" * 11 + 'Program Finished' + "-" * 11)