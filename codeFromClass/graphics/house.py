# Follow along in the team repository
# in YOUR folder & your branch

from graphics import *

def pointOffset(point, x, y):
    newX = point.x + x
    newY = point.y + y
    return Point(newX, newY)


def drawRectangle(window, point1, point2, color):
    rectangle = Rectangle(point1, point2)
    rectangle.setFill(color)
    rectangle.draw(window)


