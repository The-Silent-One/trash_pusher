from os import system
from time import ctime

def send():
    txt = "pushing on " + str(ctime()) + "\n"
    with open("history.txt","a") as f:
        f.write(txt)
    system("git add history.txt")
    system('git commit -m "automatic'+ctime()+'"')
    system("git push")

send()
