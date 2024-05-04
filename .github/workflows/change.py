import time
f = open("last_call.txt", "w")
f.write(str(round(time.time(), 3)))
f.close()
