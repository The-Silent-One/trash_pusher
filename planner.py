###size 4x5
###max letters 10
import pixelizer
import datetime

pixel = pixelizer.build_characters()

def preprocess(word):
    return word.strip().upper()

def shift(pixels):
    nb_elts = len(pixels[0])
    return [  row[i] for i in range(nb_elts) for row in pixels ]

def word_to_letter_list(word):
    if (len(word)>10):
        raise Exception("too long to show")
    if (len(word)==1):
        return shift(pixel[word[0]])
    return shift(pixel[word[0]])+shift(pixel[" "])+word_to_letter_list(word[1:])

def set_time_start():
    t = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    while(t.timetuple()[6]!=6):
        t = t+oneday
        
    return t

def create_push_calendar(start_t, letter_list):
    oneday = datetime.timedelta(days=1)
    return [i*oneday + start_t for i in range(len(letter_list)) if letter_list[i]]
    
def check_today(push_calendar):
    return datetime.date.today().__str__() in push_calendar

def next_push(push_calendar):
    day = datetime.date.today()
    oneday = datetime.timedelta(days=1)
    while day.__str__() not in push_calendar:
        day = day+oneday
    return day.__str__()

def export_push_calendar(push_calendar):
    with open("push_calendar.txt","w") as f:
        for date in push_calendar:
            f.write(date.__str__())
            f.write("\n")
            
def import_push_calendar():
    push_calendar = list()
    with open("push_calendar.txt","r") as f:
        push_calendar = [date.strip() for date in f.readlines()]
    return push_calendar

def create_file(sentance):
    word = word_to_letter_list(preprocess(sentance))
    print(word)
    t = set_time_start()
    print(t)
    p = create_push_calendar(t,word)
    print(p)
    export_push_calendar(p)
