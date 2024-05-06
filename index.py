import re
import requests
import time
import argparse

units = ["minutes", "minutes", "hour", "hours", "hours", "hours", "day", "days",      "week", "weeks"]
rangecap = [    20,        60,     65,  4*60+5, 12*60+5,   24*60, 24*60+5,   7*24*60, 7*24*60+5, 28*24*60+5]
rangebot = [     4,        14,     59,  2*60-1,  4*60-1, 12*60-1, 24*60-1, 2*24*60-1, 7*24*60-1, 14*24*60-1]
time_diff = [    5,        15,     15,      60,    4*60,   12*60,   12*60,     24*60,     24*60,    7*24*60]

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
timeElapsed = round((now-t_i)/60-0.5)

parser = argparse.ArgumentParser(description = "Dead Man's Executable")
parser.add_argument('url')
parser.add_argument('message')
args = parser.parse_args()
url, message = args.url, args.message

message = message.split("|")
# <0> Hi @!/ Hey guys   |  <1>Rye's laptop has  |  <2>stopped/ still not... |   <3>in... last     |    <3> time minutes    | <4> - could ... knows. | <5>... more.

show = True
for i in range(10):
    if timeElapsed < rangebot[i] or timeElapsed > rangecap[9]:
        break
    print(f"Testing {rangebot[i]} < {timeElapsed} < {rangecap[i]}. tE: {timeElapsed} % tD: {time_diff[i]} = {timeElapsed%time_diff[i]}")
    show = rangebot[i] < timeElapsed < rangecap[i] and timeElapsed % time_diff[i] < 5
    
    if show: #make the message
        if i > 5:
            message[0] = "Rye's laptop still hasn't responded after "
            message[1] = message[2] = message[3] = ""
            message[5] = ". Probably expected but they're not coming back guys, probably dead in a ditch. If they're not, " 
        elif timeElapsed > 59:
            message[0] = "So..."
            message[2] = "still not responded. It probably isn't coming back soon..."
            message[3] = " Time since last contact: "
            message[5] = ". If you want to know why, let's hope they can answer when you "
        elif timeElapsed > 9:
            message[0] = "Hey guys!"
            message[2] = "still not responded"
        timeElapsed = timeElapsed // (1 if i < 2 else (60 if i < 6 else (60*24 if i < 8 else 60*24*7)))
            
        if units[i][-1] != "s" and i < 2:
            message[4] = units[i]
        else:
            message[4] = str(timeElapsed) + " " + units[i]
        message = "".join(message)
        getAPI(url, message)
        break
    elif timeElapsed < rangebot[i]:
        break
