import requests
api_url = "https://discord.com/api/webhooks/1235427298971353130/oC3htsYrqPtUZ9DMHuY60zL9QnTIfJoscvtg6JKFsYxvl310-AJUKhVFb1UR7g0pJHLT"

getreq = requests.get(api_url)
message = getreq.json()
message["content"] = "Hi <@&1134833719493005352>! Rye's suddenly disappeared - could be power outage, internet outage, who knows. Kindly message them by [Messenger](<https://m.me/nokay.rra>) to find out more.\n\n" +
                "This was sent using an automated github workflow connected to their messenger. They are fortunately still alive!"
requests.post(api_url, message)
