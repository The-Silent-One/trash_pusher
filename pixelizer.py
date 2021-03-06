from graphics import *
from time import *
x , y = 490,490
nb = 7
space = x/nb
wait = True
speed=10
font_size = [7,7]
char_list= ["A","B","C","D","E","F","G","H","I","J"
            ,"K","L","M","N","O","P","Q","R","S","T"
            ,"U","V","W","X","y","Z"
            ,"0","1","2","3","4","5","6","7","8","9"]

def gridding(win):
    
    for i in range(0,x+int(space),int(space)):
        Line(Point(i,0),Point(i,y)).draw(win)
        if(wait):
            sleep(0.1/speed)
    
    for i in range(0,y+int(space),int(space)):
        Line(Point(0,i),Point(x,i)).draw(win)
        if(wait):
            sleep(0.1/speed)

def char_converter():
    pixel = dict()
    pixel[char_list[0]] = [ [0,0,0,0,0,0],
                            [0,0,1,1,0,0],
                            [0,1,0,0,1,0],
                            [0,1,1,1,1,0],
                            [0,1,0,0,1,0],
                            [0,1,0,0,1,0],
                            [0,0,0,0,0,0] ]
    pixel[char_list[1]] = [ [0,0,0,0,0,0],
                            [0,1,1,1,0,0],
                            [0,1,0,0,1,0],
                            [0,1,1,1,1,0],
                            [0,1,0,0,1,0],
                            [0,1,1,1,0,0],
                            [0,0,0,0,0,0] ]
    pixel[char_list[2]] = [ [0,0,0,0,0,0],
                            [0,0,1,1,0,0],
                            [0,1,0,0,1,0],
                            [0,1,0,0,0,0],
                            [0,1,0,0,1,0],
                            [0,0,1,1,0,0],
                            [0,0,0,0,0,0] ]
    pixel[char_list[3]] = [ [0,0,0,0,0,0],
                            [0,1,1,1,0,0],
                            [0,1,0,0,1,0],
                            [0,1,0,0,1,0],
                            [0,1,0,0,1,0],
                            [0,1,1,1,0,0],
                            [0,0,0,0,0,0] ]
    pixel[char_list[4]] = [ [0,0,0,0,0,0],
                            [0,1,1,1,1,0],
                            [0,1,0,0,0,0],
                            [0,1,1,1,0,0],
                            [0,1,0,0,0,0],
                            [0,1,1,1,1,0],
                            [0,0,0,0,0,0] ]
    pixel[char_list[5]] = [ [0,0,0,0,0,0],
                            [0,1,1,1,1,0],
                            [0,1,0,0,0,0],
                            [0,1,1,1,0,0],
                            [0,1,0,0,0,0],
                            [0,1,0,0,0,0],
                            [0,0,0,0,0,0] ]
    pixel[char_list[6]] = [ [0,0,0,0,0,0],
                            [0,0,1,1,0,0],
                            [0,1,0,0,0,0],
                            [0,1,0,1,1,0],
                            [0,1,0,0,1,0],
                            [0,0,1,1,0,0],
                            [0,0,0,0,0,0] ]
    pixel[char_list[7]] = [ [0,0,0,0,0,0],
                            [0,1,0,0,1,0],
                            [0,1,0,0,1,0],
                            [0,1,1,1,1,0],
                            [0,1,0,0,1,0],
                            [0,1,0,0,1,0],
                            [0,0,0,0,0,0] ]
    pixel[char_list[8]] = [ [0,0,0,0,0,0],
                            [0,0,0,1,0,0],
                            [0,0,0,1,0,0],
                            [0,0,0,1,0,0],
                            [0,0,0,1,0,0],
                            [0,0,0,1,0,0],
                            [0,0,0,0,0,0] ]
    pixel[char_list[9]] = [ [0,0,0,0,0,0],
                            [0,0,0,0,1,0],
                            [0,0,0,0,1,0],
                            [0,0,0,0,1,0],
                            [0,1,0,0,1,0],
                            [0,0,1,1,0,0],
                            [0,0,0,0,0,0] ]
    pixel[char_list[10]] = [ [0,0,0,0,0,0],
                             [0,1,0,0,1,0],
                             [0,1,0,1,0,0],
                             [0,1,1,0,0,0],
                             [0,1,0,1,0,0],
                             [0,1,0,0,1,0],
                             [0,0,0,0,0,0] ]
    pixel[char_list[11]] = [ [0,0,0,0,0,0],
                             [0,1,0,0,0,0],
                             [0,1,0,0,0,0],
                             [0,1,0,0,0,0],
                             [0,1,0,0,0,0],
                             [0,1,1,1,1,0],
                             [0,0,0,0,0,0] ]
    pixel[char_list[12]] = [ [0,0,0,0,0,0],
                             [0,1,0,0,1,0],
                             [0,1,1,1,1,0],
                             [0,1,0,0,1,0],
                             [0,1,0,0,1,0],
                             [0,1,0,0,1,0],
                             [0,0,0,0,0,0] ]
    pixel[char_list[13]] = [ [0,0,0,0,0,0],
                             [0,1,0,0,1,0],
                             [0,1,1,0,1,0],
                             [0,1,0,1,1,0],
                             [0,1,0,0,1,0],
                             [0,1,0,0,1,0],
                             [0,0,0,0,0,0] ]
    pixel[char_list[14]] = [ [0,0,0,0,0,0],
                             [0,0,1,1,0,0],
                             [0,1,0,0,1,0],
                             [0,1,0,0,1,0],
                             [0,1,0,0,1,0],
                             [0,0,1,1,0,0],
                             [0,0,0,0,0,0] ]
    pixel[char_list[15]] = [ [0,0,0,0,0,0],
                             [0,1,1,1,0,0],
                             [0,1,0,0,1,0],
                             [0,1,1,1,0,0],
                             [0,1,0,0,0,0],
                             [0,1,0,0,0,0],
                             [0,0,0,0,0,0] ]
    pixel[char_list[16]] = [ [0,0,0,0,0,0],
                             [0,0,1,1,0,0],
                             [0,1,0,0,1,0],
                             [0,1,0,0,1,0],
                             [0,1,0,1,1,0],
                             [0,0,1,1,1,0],
                             [0,0,0,0,0,0] ]
    pixel[char_list[17]] = [ [0,0,0,0,0,0],
                             [0,1,1,1,0,0],
                             [0,1,0,0,1,0],
                             [0,1,1,1,1,0],
                             [0,1,0,1,0,0],
                             [0,1,0,0,1,0],
                             [0,0,0,0,0,0] ]
    pixel[char_list[18]] = [ [0,0,0,0,0,0],
                             [0,0,1,1,1,1],
                             [0,1,0,0,0,0],
                             [0,0,1,1,1,0],
                             [0,0,0,0,0,1],
                             [0,1,1,1,1,0],
                             [0,0,0,0,0,0] ]
    pixel[char_list[19]] = [ [0,0,0,0,0,0],
                             [0,0,1,1,1,0],
                             [0,0,0,1,0,0],
                             [0,0,0,1,0,0],
                             [0,0,0,1,0,0],
                             [0,0,0,1,0,0],
                             [0,0,0,0,0,0] ]
    pixel[char_list[20]] = [ [0,0,0,0,0,0],
                             [0,1,0,0,1,0],
                             [0,1,0,0,1,0],
                             [0,1,0,0,1,0],
                             [0,1,0,0,1,0],
                             [0,0,1,1,0,0],
                             [0,0,0,0,0,0] ]
    pixel[char_list[21]] = [ [0,0,0,0,0,0],
                             [0,1,0,1,0,0,0],
                             [0,1,0,1,0,0],
                             [0,1,0,1,0,0],
                             [0,1,0,1,0,0],
                             [0,0,1,0,0,0],
                             [0,0,0,0,0,0] ]
    pixel[char_list[22]] = [ [0,0,0,0,0,0],
                             [0,1,0,0,1,0],
                             [0,1,0,0,1,0],
                             [0,1,0,0,1,0],
                             [0,1,1,1,1,0],
                             [0,1,0,0,1,0],
                             [0,0,0,0,0,0] ]
    pixel[char_list[23]] = [ [0,0,0,0,0,0],
                             [0,1,0,0,1,0],
                             [0,1,0,0,1,0],
                             [0,0,1,1,0,0],
                             [0,1,0,0,1,0],
                             [0,1,0,0,1,0],
                             [0,0,0,0,0,0] ]
    pixel[char_list[24]] = [ [0,0,0,0,0,0],
                             [0,1,0,1,0,0],
                             [0,1,0,1,0,0],
                             [0,0,1,0,0,0],
                             [0,0,1,0,0,0],
                             [0,0,1,0,0,0],
                             [0,0,0,0,0,0] ]
    pixel[char_list[25]] = [ [0,0,0,0,0,0],
                             [0,1,1,1,1,0],
                             [0,0,0,0,1,0],
                             [0,0,1,1,0,0],
                             [0,1,0,0,0,0],
                             [0,1,1,1,1,0],
                             [0,0,0,0,0,0] ]
    pixel[char_list[26]] = [ [0,0,0,0,0,0],
                             [0,0,1,1,0,0],
                             [0,1,0,1,1,0],
                             [0,1,1,0,1,0],
                             [0,1,0,0,1,0],
                             [0,0,1,1,0,0],
                             [0,0,0,0,0,0] ]
    pixel[char_list[27]] = [ [0,0,0,0,0,0],
                             [0,0,0,1,0,0],
                             [0,0,1,1,0,0],
                             [0,0,0,1,0,0],
                             [0,0,0,1,0,0],
                             [0,0,0,1,0,0],
                             [0,0,0,0,0,0] ]
    pixel[char_list[28]] = [ [0,0,0,0,0,0],
                             [0,0,1,1,0,0],
                             [0,1,0,0,1,0],
                             [0,0,0,1,0,0],
                             [0,0,1,0,0,0],
                             [0,1,1,1,1,0],
                             [0,0,0,0,0,0] ]
    pixel[char_list[29]] = [ [0,0,0,0,0,0],
                             [0,1,1,1,0,0],
                             [0,0,0,0,1,0],
                             [0,0,1,1,0,0],
                             [0,0,0,0,1,0],
                             [0,1,1,1,0,0],
                             [0,0,0,0,0,0] ]
    pixel[char_list[30]] = [ [0,0,0,0,0,0],
                             [0,1,0,0,1,0],
                             [0,1,0,0,1,0],
                             [0,1,1,1,1,0],
                             [0,0,0,0,1,0],
                             [0,0,0,0,1,0],
                             [0,0,0,0,0,0] ]
    pixel[char_list[31]] = [ [0,0,0,0,0,0],
                             [0,1,1,1,1,0],
                             [0,1,0,0,0,0],
                             [0,1,1,1,0,0],
                             [0,0,0,0,1,0],
                             [0,1,1,1,0,0],
                             [0,0,0,0,0,0] ]
    pixel[char_list[32]] = [ [0,0,0,0,0,0],
                             [0,0,1,1,0,0],
                             [0,1,0,0,0,0],
                             [0,1,1,1,0,0],
                             [0,1,0,0,1,0],
                             [0,0,1,1,0,0],
                             [0,0,0,0,0,0] ]
    pixel[char_list[33]] = [ [0,0,0,0,0,0],
                             [0,1,1,1,1,0],
                             [0,0,0,0,1,0],
                             [0,0,0,1,0,0],
                             [0,0,0,1,0,0],
                             [0,0,0,1,0,0],
                             [0,0,0,0,0,0] ]
    pixel[char_list[34]] = [ [0,0,0,0,0,0],
                             [0,0,1,1,0,0],
                             [0,1,0,0,1,0],
                             [0,0,1,1,0,0],
                             [0,1,0,0,1,0],
                             [0,0,1,1,0,0],
                             [0,0,0,0,0,0] ]
    pixel[char_list[35]] = [ [0,0,0,0,0,0],
                             [0,0,1,1,0,0],
                             [0,1,0,0,1,0],
                             [0,0,1,1,1,0],
                             [0,0,0,0,1,0],
                             [0,0,1,1,0,0],
                             [0,0,0,0,0,0] ]
    return pixel

def normalize(pixel):
    for letter in pixel.values():
        i = 0
        while(i<len(letter[0])):
            col_sum = sum([p[i] for p in letter])
            if (col_sum==0):
                for p in letter:
                    p.pop(i)
                i = i - 1
            i = i + 1
        #print(letter)
        #print("***")
    return pixel

def pixelizer(win,pixel,char,size=[nb,nb],slider=[0,0]):
    blocks = []
    for i in range(min(nb,len(pixel[char]))):
        for j in range(min(nb,len(pixel[char][0]))):
            try:
                if(pixel[char][ i % font_size[0] ][ j % font_size[1] ] == 1):
                    blocks.append(Block(win,j % size[1] + slider[0] , i % size[0] +slider[1]))
            except Exception as e:
                pass
                #print(e)
                #print( "i = "+str(i)+" j = "+str(j))
    animateBulk(win,blocks)
    return blocks

def destroy(blocks):
    for b in blocks:
        b.animateD()
        
def animateBulk(win,blocks):
    for b in blocks:
        b.animateD()
    sleep(0.5/speed)
    for b in blocks:
        b.animateU(win)
        
class Block:
    color ="#544e3e"
    def draw(self,win):
        self.shape = Polygon(Point(self.x,self.y),
                          Point(self.x+space,self.y),
                          Point(self.x+space,self.y+space),
                          Point(self.x,self.y+space))
        self.shape.draw(win)
        self.shape.setFill(self.color)
        
    def __init__(self,win,pos_x,pos_y):
        if(pos_x < 0):
            pos_x = 0
        elif(pos_x >= nb):
            pos_x = nb -1

        if(pos_y < 0):
            pos_y = 0
        elif(pos_y >= nb):
            pos_y = nb -1

        self.pos_x = int(pos_x)
        self.pos_y = int(pos_y)
        self.x = self.pos_x * space
        self.y = self.pos_y * space
        self.draw(win)
        
    def animateD(self):
        self.shape.undraw()
    def animateU(self,win):
        self.shape.draw(win)
        
def build():
    win = GraphWin("Grid",x,y)
    gridding(win)
    return win

def visualize(win,pixel):
    for char in char_list:
        b=pixelizer(win,pixel,char)
        #win.getMouse()
        sleep(3/speed)
        destroy(b)
        
def build_characters():
    pixel = char_converter()
    pixel = normalize(pixel)
    pixel[" "] = [[0], [0], [0], [0], [0], [0], [0]]
    return pixel

#win = build()
#visualize(win,pixel)
