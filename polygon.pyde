def setup():
    size(600,600)
    
def draw():
    translate(width/2,height/2)
    polygon(8,100) #sides,vertice units from center
    
def polygon(sides, size):
    '''draws a polygon given the number of sides and length from the center.'''
    beginShape()
    for i in range(sides):
        step = radians(360/sides)
        vertex(size*cos(i*step), size*sin(i*step))
    endShape(CLOSE)
