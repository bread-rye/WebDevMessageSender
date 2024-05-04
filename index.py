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
last_call.close()

now = time.time()
timeElapsed = (now-t_i)/60

parser = argparse.ArgumentParser(description = "Dead Man's Executable")
parser.add_argument('url')
parser.add_argument('message')
args = parser.parse_args()
url, message = args.url, args.message
message = message.split("|")
message[1] = str(round(timeElapsed))
message = "".join(message)

if timeElapsed>5:
    getAPI(url, message)
print(now)
