# Follow along in the team repository
# in YOUR folder & your branch

from graphics import *
import random

def pointOffset(point, x, y):
    newX = point.x + x
    newY = point.y + y
    return Point(newX, newY)


def drawCloud(window, p):
    p2 = Point(p.x + 50, p.y - 10)
    bottomOval = Oval(p, p2)
    bottomOval.setFill("grey")
    bottomOval.setOutline("grey")
    bottomOval.draw(window)
    
    bigRadius = 15
    bigCircle = Circle(Point(p2.x - bigRadius, p.y - bigRadius), bigRadius)
    bigCircle.setFill("grey")
    bigCircle.setOutline("grey")
    bigCircle.draw(window)
    
    littleRadius = 8
    littleCircle = Circle(Point(p.x + 15, p.y - littleRadius), littleRadius)
    littleCircle.setFill("grey")
    littleCircle.setOutline("grey")
    littleCircle.draw(window)

def drawRandomCloud(window):
    x = random.randint(0, 500)
    y = random.randint(50, 150)
    drawCloud(window, Point(x,y))

def drawTriangle(window, point1, point2, point3, color):
    triangle = Polygon(point1, point2, point3)
    triangle.setFill(color)
    triangle.draw(window)

def drawRoof(window):
    drawTriangle(window, Point(100,150), Point(400, 150), Point(250, 50), "red")

'''
# test
win = GraphWin("My Circle", 500, 500)
drawRoof(win)
#drawCloud(win, Point(50,50))
drawRandomCloud(win)
'''
