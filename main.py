import json
import requests
import time
import threading
import random
import string
import colorama 
from colorama import init
from termcolor import colored
from colorama import Fore, Back, Style
init(autoreset=True)
print("Google Slides Finder by THECRAZEDPOTATTO")
print("")
def sfinder():
  link = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=44))
  eslide = (f"https://docs.google.com/presentation/d/{link}/edit")
  resp = requests.get(eslide)
  state = resp.status_code
  if state == 404:
    print(Fore.RED + "[NOT VALID] "+eslide)
  if state == 200:
    print(Fore.GREEN + "[VALID] "+eslide)
    with open('valid.txt', 'w') as f:
      f.write(eslide)
def dfinder():
  link = ''.join(random.choices(string.ascii_uppercase + string.digits + string.ascii_lowercase, k=44))
  edoc = (f"https://docs.google.com/document/d/{link}/edit")
  resp = requests.get(edoc)
  state = resp.status_code
  if state == 404:
    print(Fore.RED + "[NOT VALID] "+edoc)
  if state == 200:
    print(Fore.GREEN + "[VALID] "+edoc)
    with open('valid.txt', 'w') as f:
      f.write(edoc)
input("Press Enter To Find Docs and Slides >> ")
while(True):
  sfinder()
  dfinder()
  

