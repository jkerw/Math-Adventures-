circleList = [] #save the locations of external ellipse

def setup():
    size(600,600)

r1=100
r2=10
t=0

def draw():
    global t, circleList
    background(200)
    translate(width/4,height/4) #moves a given distance from center point
    noFill()
    stroke(0)
    ellipse(0,0,2*r1,2*r1)
    
    #travelling ellipse
    fill(255,0,0)
    y = r1*sin(t)
    x = r1*cos(t)
    circleList = [y] + circleList[:249]
    ellipse(x,y,r2,r2)
    
    stroke(0,255,0)
    line(x,y,200,y)
    fill(0,255,0)
    ellipse(200,y,10,10)
    for iter, circ in enumerate(circleList):
        ellipse(200+iter,circ,5,5)
    t+= 0.05
    
