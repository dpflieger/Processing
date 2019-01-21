add_library("Sound")
add_library("minim")
import os

WINDOW_HEIGHT = 800
WINDOW_WIDTH = 1400
FPS = 60
BALL_SIZE = 20
GRAVITY = 0.1

class Terrain(object):
    count = 0
    names = []
    def __init__(self, name):
        self.number = Terrain.count
        self.name = name
        Terrain.count += 1
        Terrain.names.append(name)

class Ball(object):
    def __init__(self, c, x, y, _width, _height, xspeed, yspeed):
        self.c = c
        self.x = x
        self.y = y
        self._width = _width
        self._height = _height
        self.xspeed = xspeed
        self.yspeed = yspeed
        
    def display(self):
        fill(self.c)
        ellipse(self.x, self.y, self._width, self._height)
        
    def move(self):
        self.x += self.xspeed
        self.y += self.yspeed
        if self.x < 0 or self.x > width:
            self.xspeed *= -1
        if self.y < 0  or self.y > height:
            self.yspeed *= -1
        print(self.x, self.y)

class Rectangle(object):
    def __init__(self, x, y, _width, _height):
        self.x = x
        self.y = y
        self._width = _width
        self._height = _height
    
class Car(object):

    def __init__(self, c, x, y, _width, _height, xspeed, yspeed, velocity):
        self.c = c
        self.x = x
        self.y = y
        self._width = _width
        self._height = _height
        self.xspeed = xspeed
        self.yspeed = yspeed
        self.velocity = velocity

    def display(self):
        stroke(0)
        fill(self.c)
        rectMode(CENTER)
        rect(self.x, self.y, self._width, self._height)
    
    def move(self):
        if (self.x > height):
            self.x = height
        if (self.x < 0):
            self.x = 0
        self.x = mouseX
    
    
myBall = Ball(color(255, 30, 30), 200, 100, 25, 25, 0.1, 0.1)
myBall2 = Ball(color(255), 600, 500, 30, 30, 1, 1)
myCar = Car(color(255, 0, 0), WINDOW_WIDTH/2, WINDOW_HEIGHT - 50, 100, 10, 1, 1, 0.1)


def collision(ball, car):
    
    # check x movement
    if(ball.x + ball._width + ball.xspeed > ball.x and ball.x + ball.xspeed < car.x + car._width and ball.y + ball._height > car.y and ball.y < car.y + car._height):
        ball.xspeed *= -1
    # check y movement
    if(ball.x + ball._width > car.x and ball.x < car.x + car._width and ball.y + ball._height + ball.yspeed > car.y and ball.y + ball.yspeed < car.y + car._height):
        ball.yspeed *= -1
        
    ball.x += ball.xspeed
    ball.y += ball.yspeed


def setup():
    global img
    global sf
    img = loadImage("wallpaper.jpg")
    #sf = SoundFile(this, "sample_test.mp3")
    #sf.loop()
    #player = Minim(this).loadFile("sample_test.mp3")
    #player.loop()
    global terrains
    terrains = [(i, 200, 55, 55) for i in range(200, width - 120, 60)]
    terrains.extend([(i, 300, 55, 55) for i in range(200, width - 120, 60)])
    
    size(WINDOW_WIDTH, WINDOW_HEIGHT)

def draw():
    image(img, 0, 0) 
    for param in terrains:
        rectangle = Rectangle(*param)
        collision(myBall,rectangle)
        
        fill(255, 0, 0)
        rect(rectangle.x, rectangle.y, rectangle._width, rectangle._height)
    
    myBall.display()
    myBall.move()
    myCar.move()
    myCar.display()
 
    #myBall.move()
    myBall2.move()
    myBall2.display()
    collision(myBall,myCar)
    



  
  
