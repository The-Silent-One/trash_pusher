import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class Calendar(QCalendarWidget):
    width = 400
    height = 400
    
    def __init__(self,parent=None):
        super(Calendar, self).__init__(parent)
        self.setWindowTitle("Trash Pusher Calendar")
        self.setGeometry(0,0,self.width,self.height)
        self.setGridVisible(True)
        self.resize(self.width,self.height)
        self.dates = self.getMarkedDays()
        self.color = QColor(212,61,13)
        
    def getMarkedDays(self):
        
        lines = list()
        with open("push_calendar.txt","r") as f:
            lines = f.readlines()
        
        dates = [ l.strip().split("-") for l in lines ]
        dates = [ [int(d) for d in block ] for block in dates]
        dates = [ QDate(d[0],d[1],d[2])for d in dates]
        
        return dates
    
    def paintCell(self, painter, rect, date):
        QCalendarWidget.paintCell(self, painter, rect, date)
        if date in self.dates:
            painter.fillRect(rect,self.color)
            posx = rect.x()+int(2*rect.width()/3)
            posy = rect.y()+int(rect.height()/3)
            painter.drawText(posx,posy,str(date.day()))
            
def create_app():
    app = QApplication(sys.argv)
    
    cal = Calendar()
    cal.show()
    
    sys.exit(app.exec_())
    
create_app()
