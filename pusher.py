from os import system
from time import ctime
from planner import *
from sender import *
import calendar

def daysAction():
    p = import_push_calendar()
    #print(p)
    if(check_today(p)):
        txt = "pushing on " + str(ctime()) + "\n"
        with open("history.txt","a") as f:
            f.write(txt)
        system("git add history.txt")
        system('git commit -m "automatic'+ctime()+'"')
        system("git push")
    
    ##next push
    day = next_push(p)
    send("next is ["+day+"]","next day to push is "+day+"<br>Be sure to connect that day")

daysAction()
