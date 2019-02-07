w, angle = 100, 0

class Curve():
    
    def __init__(self):
        self.path = []
        self.current = PVector()
               
    def add_point(self):
        self.path.append(self.current)
            
    def setY(self, y):
        self.current.y = y
        
    def setX(self, x):
        self.current.x = x
         
    def reset(self):
        self.path = []
        
    def show(self):
        stroke(255)
        strokeWeight(2)
        noFill()
        beginShape()
        for v in self.path:
            vertex(v.x, v.y)
        endShape()
        strokeWeight(8)
        point(self.current.x, self.current.y)
        self.current = PVector ()  

def setup():
    frameRate(30)
    size(800, 800)
    global cols, rows, curves, colors
    cols = width / w - 1 
    rows = height / w - 1
    curves = [[Curve() for i in range(rows)] for j in range(cols)]
    colors = [color(random(255), random(255), random(255)) for i in range(cols)]

def draw():
    global angle, test, w
    background(0)
    d = w - 0.2 * w
    r = d / 2
    noFill()
    stroke(255)
    for i in range(cols):
        cx = w + i * w + w / 2
        cy = w / 2
        strokeWeight(2)
        stroke(colors[i])
        ellipse(cx, cy, d, d)
        x = r * cos(angle * (i + 1) - HALF_PI)
        y = r * sin(angle * (i + 1) - HALF_PI)
        strokeWeight(8)
        stroke(255)
        point(cx + x, cy + y)
        stroke(colors[i])
        strokeWeight(1)
        line(cx + x, 0, cx + x, height)
        for j in range(rows): 
            curves[j][i].setX(cx + x)
    noFill()
    stroke(255)
    for j in range(rows):
        cx = w / 2
        cy = w + j * w + w / 2
        strokeWeight(2)
        stroke(colors[j])
        ellipse(cx, cy, d, d)
        x = r * cos(angle * (j + 1) - HALF_PI)
        y = r * sin(angle * (j + 1) - HALF_PI)
        strokeWeight(8)
        stroke(255)
        point(cx + x, cy + y)
        stroke(colors[j])
        strokeWeight(1)
        line(0, cy + y, width, cy + y)
        for i in range(cols):
            curves[j][i].setY(cy + y)

    for j in range(rows):
        for i in range(cols):
            curves[j][i].add_point()
            curves[j][i].show()
            
    angle -= 0.015
    if (angle < -TWO_PI):
        for j in range(rows):
            for i in range(cols):
                curves[j][i].reset()

        #saveFrame("lissajous#####.png");
        angle = 0
    print(angle)


  
