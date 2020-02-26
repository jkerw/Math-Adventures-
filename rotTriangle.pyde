def setup():
    size(600,600)
    rectMode(CENTER)
    colorMode(HSB)
t = 0

def draw():
    background(255)
    global t
    translate(width/2,height/2)
  
    for i in range(90):
        rotate(radians(360/90))
        pushMatrix() #saves the orientation  
        #goes to circumference of circle
        translate(200,0) 
        #spins each triangle
        rotate(radians(t+2*i*360/90))
        tri(100)
        popMatrix() #return to saved orientation
        strokeWeight(2)
        stroke(3*i, 255, 255)
    t += 0.5
    
def tri(length):
    '''draws an equilateral triangle around center of triangle.'''
    noFill()

    triangle(0,-length, 
             -length*sqrt(3)/2, length/2, 
             length*sqrt(3)/2, length/2)
    
