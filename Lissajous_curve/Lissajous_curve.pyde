add_library('VideoExport')
add_library('dashedlines')
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
        
    def show(self, colors, i, j):
        print(mix_color(colors[i], colors[j]))
        stroke(*mix_color(colors[i], colors[j]))
        strokeWeight(2)
        noFill()
        beginShape()
        for v in self.path:
            vertex(v.x, v.y)
        endShape()
        strokeWeight(8)
        point(self.current.x, self.current.y)
        self.current = PVector()  

def mix_color(c1, c2):
    return [((c1[idx] + c2[idx]) / 2) for idx in range(3)]

def setup():
    frameRate(60)
    size(800, 800)
    global cols, rows, curves, colors, dash
    cols = width / w - 1 
    rows = height / w - 1
    dash = DashedLines(this)
    dash.pattern(5, 5, 5, 5)
    videoExport = VideoExport(this)
    videoExport.startMovie()
    curves = [[Curve() for i in range(rows)] for j in range(cols)]
    colors = [(random(255), random(255), random(255)) for i in range(cols)]
    

def draw():
    global angle, test, w
    background(20)
    d = w - 0.2 * w
    r = d / 2
    noFill()
    stroke(255)
    for i in range(cols):
        cx = w + i * w + w / 2
        cy = w / 2
        strokeWeight(2)
        stroke(*colors[i])
        ellipse(cx, cy, d, d)
        x = r * cos(angle * (i + 1) - HALF_PI)
        y = r * sin(angle * (i + 1) - HALF_PI)
        strokeWeight(8)
        stroke(255)
        point(cx + x, cy + y)
        stroke(*colors[i])
        strokeWeight(1)
        dash.line(cx + x, cy + y, cx + x, height)
        for j in range(rows): 
            curves[j][i].setX(cx + x)
    noFill()
    stroke(255)
    for j in range(rows):
        cx = w / 2
        cy = w + j * w + w / 2
        strokeWeight(2)
        stroke(*colors[j])
        ellipse(cx, cy, d, d)
        x = r * cos(angle * (j + 1) - HALF_PI)
        y = r * sin(angle * (j + 1) - HALF_PI)
        strokeWeight(8)
        stroke(255)
        point(cx + x, cy + y)
        stroke(*colors[j])
        strokeWeight(1)
        dash.line(cx + x, cy + y, width, cy + y)
        for i in range(cols):
            curves[j][i].setY(cy + y)

    for j in range(rows):
        for i in range(cols):
            curves[j][i].add_point()
            curves[j][i].show(colors, i, j)
            
    angle += 0.010
    if (angle > TWO_PI):
        for j in range(rows):
            for i in range(cols):
                curves[j][i].reset()

        angle = 0 # reset after 2 tours 2PI
    #saveFrame("Lissajous_curve####.png");
    videoExport.saveFrame()
    
def keyPressed():
  if (key == 'q'):
    videoExport.endMovie()
    exit()

  
