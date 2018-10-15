#!/usr/bin/python3
from tkinter import *
from math import cos, sin, radians
from operator import add

class DrawingCanvas(Canvas):
    def rotate(self,amount):
        self.rotation = (self.rotation + amount)
    def Vectorize(self, length, rotation=None):
        if rotation is None:
            rotation = self.rotation
        return (length*-sin(radians(rotation)), length*-cos(radians(rotation)))
    
    def drawLine(self, length):
        newPos = tuple(map(add,self.pos,self.Vectorize(length))) #use map to add equal indexes, return to type tuple
        self.create_line(self.pos[0], self.pos[1], newPos[0], newPos[1], width=1)
        self.pos = newPos
        root.update()
        
    def constructSnowflake(self,N,D,alpha):
        if N==1:
            self.drawLine(D)
        else:

            self.constructSnowflake(N-1,D/3,alpha)
            self.rotate(-ANGLE)
            self.constructSnowflake(N-1,D/3,alpha)
            self.rotate(2*ANGLE)
            self.constructSnowflake(N-1,D/3,alpha)
            self.rotate(-ANGLE)
            self.constructSnowflake(N-1,D/3,alpha)
                
    def __init__(self,parent,*args,**kwargs):
        Canvas.__init__(self,parent,*args,**kwargs)
        self.parent = parent
        self.grid(column=1,row=1,sticky=W);
        self.go = 0

def goHandler():
    global dc
    del(dc)
    dc = DrawingCanvas(root, width=WIDTH,height=HEIGHT)
    dc.grid(column=0,row=3, sticky=W, columnspan=10)
    dc.pos = (WIDTH/1.6, HEIGHT/1.3)
    dc.rotation = 0
    dc.constructSnowflake(int(depth.get()),LENGTH,int(ANGLE))
    
if __name__ == "__main__":
    root = Tk()
    root.title("Snowflake drawer")
    WIDTH = 900
    HEIGHT = 700
    LEFTMOST = 0
    TOPMOST = 0
    LENGTH = 400
    ANGLE = 60

    Label(root, text="Enter fractal depth:").grid(column=0,row=0,sticky=W)
    depth = Entry(root)
    depth.insert(0,"5")
    depth.grid(column=1,row=0,sticky=W)

    branchCount = StringVar()
    branchCount.set("0")
    
    Button(root, text="Go!", command=goHandler).grid(column=1, row=2,sticky=W)
    
    dc = DrawingCanvas(root, width=WIDTH,height=HEIGHT)
    dc.grid(column=0,row=3, sticky=W, columnspan=10)
    root.mainloop()
    
    print("job done")
    i=1
    sum = 0
