import re
import requests
import time
import argparse

def decode(s):
    return decodeURIComponent(re.sub("[0-9a-f]{2}", "%$&"))

def callAPI(url, message, body):
    preq = requests.post(url, json=body | {"content":message})
    print(preq)

def getAPI(u, m):
    greq = requests.get(u)
    print(greq)
    callAPI(u, m, greq.json())

last_call = open("last_call.txt", "r+")
t_i = float(last_call.readline())
now = time.time()
timeElapsed = (now-t_i)/60

parser = argparse.ArgumentParser(description = "Dead Man's Executable")
parser.add_argument('url')
parser.add_argument('message')
args = parser.parse_args()
url, message = args.url, args.message

if timeElapsed>5:
    getAPI(url, message)
else:
    last_call.seek(0)
    last_call.write(str(now))
print(now)
last_call.close()
