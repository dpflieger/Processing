add_library("Sound")
add_library("minim")
import os

class Ball(object):
    def __init__(self, c, x, y, xspeed, yspeed):
        self.c = c
        self.x = x
        self.y = y
        self.xspeed = xspeed
        self.yspeed = yspeed
        
    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, 30, 30)
        
    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        if self.x < 0 or self.x > width:
            self.xspeed *= -1
        if self.y < 0  or self.y > height:
            self.yspeed *= -1

class Car(object):
# The Constructor is defined with arguments.
    def __init__(self, c, xpos, ypos, xspeed):
        self.c = c
        self.xpos = xpos
        self.ypos = ypos
        self.xspeed = xspeed

    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.xpos, self.ypos, 20, 10)
    
    def drive(self):
        self.xpos = self.xpos + self.xspeed
        if self.xpos > width:
            self.xpos = 0

    

myBall = Ball(color(255, 30, 30), 200, 100, 4, 5)
myBall2 = Ball(color(255) , 600, 500, 1, 1)
myCar1 = Car(color(255, 0, 0), 0, 100, 2)

def setup():
    global img
    global sf
    img = loadImage("wallpaper.jpg")
    #sf = SoundFile(this, "sample_test.mp3")
    #sf.loop()
    player = Minim(this).loadFile("sample_test.mp3")
    player.loop()
    size(1400, 800)


   
def draw():
    image(img, 0, 0)
    myCar1.drive()
    myCar1.display()
    myBall.display()
    myBall.move()
    myBall2.move()
    myBall2.display()
    



  
  
