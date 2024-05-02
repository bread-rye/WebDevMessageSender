import time
now = time.time()

f = open("last_call.txt", "r+")
t_i = float(f.readline())
time_elapsed = (now - t_i)/60

if time_elapsed > 5:
  import requests
  api_url = "https://discord.com/api/webhooks/1235427298971353130/oC3htsYrqPtUZ9DMHuY60zL9QnTIfJoscvtg6JKFsYxvl310-AJUKhVFb1UR7g0pJHLT"
  getreq = requests.get(api_url)
  message = getreq.json()
  message["content"] = f"Hi <@&1134833719493005352>! Rye's laptop has stopped responding in the last {round(time_elapsed-0.5)} minutes - could be power outage" + \
                  ", internet outage, who knows. Kindly message them by [Messenger](<https://m.me/nokay.rra>) to find out more."
  requests.post(api_url, message)
else:
  f.seek(0)
  f.write(str(now))
f.close()
