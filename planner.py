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
    return shift(pixel[word[0]])+shift(pixel[" "])+word_to_agenda(word[1:])

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
    return datetime.date.today() in push_calendar

def export_push_calendar(push_calendar):
    with open("push_calendar.txt","w") as f:
        for date in push_calendar:
            f.write(date.__str__())
            f.write("\n")

a = word_to_letter_list(preprocess("a"))
print(a)
t = set_time_start()
print(t)
p = create_push_calendar(t,a)
print(p)
print(check_today(p))
export_push_calendar(p)
