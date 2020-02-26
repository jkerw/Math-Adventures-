from math import sqrt

def cubicEquation(x):
    return 6*x**3 + 31*x**2 + 3*x - 10

def bruteForceMath():
    x = -100
    while x < 100:
        if g(x) == 0:
            print("x= ", x)
        x+=1

def firstDegree(a,b,c,d):
    '''solves equations of the form ax+b=cx+d'''
    return (d-b)/(a-c)

def quad(a,b,c):
    '''returns the solns of an equation of the form ax**2+bx+c=0'''
    pos_result = (-b + sqrt(b**2-4*a*c))/(2*a)
    neg_result = (-b - sqrt(b**2-4*a*c))/(2*a)
    return pos_result, neg_result
