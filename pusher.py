import os
import time

def send():
    txt = "pushing on " + str(time.ctime()) + "\n"
    with open("history.txt","a") as f:
        f.write(txt)
    os.system("git add history.txt")
send()
