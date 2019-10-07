# Follow along in the team repository
# in YOUR folder & your branch

from graphics import *

def pointOffset(point, x, y):
    newX = point.x + x
    newY = point.y + y
    return Point(newX, newY)


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
'''
