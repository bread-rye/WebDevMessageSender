from datetime import datetime
time = datetime.now
f = open("last_call.txt", "w")
f.write(str(round(time, 3)))
f.close()
