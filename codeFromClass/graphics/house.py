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


def drawPane(window, point):
    drawRectangle(window, point, pointOffset(point, 40, 40), "lightgrey")

def rowOfBricks(window, x, y, color, heightOfBrick):
    widthOfBrick = 20   
    while (x < 350):
        topLeftCorner = Point(x,y)
        bottomRightCorner = Point(x+widthOfBrick, y + heightOfBrick)
        drawRectangle(window, topLeftCorner, bottomRightCorner, color)
        x = x + widthOfBrick


def drawHouse(window, color):
    drawRectangle(window, Point(150,150), Point(350,350), color)

    '''
    heightOfBrick = 10
    x = 150
    y = 150
    while (y < 350):        
        rowOfBricks(window, x, y, color, heightOfBrick)
        y = y + heightOfBrick
    '''
    panes = [Point(175, 175), Point(175, 275), Point(275, 175), Point(275, 275), Point(225,310), Point(225,270)]
    for pane in panes:
      drawPane(window, pane)


'''
# for testing
win = GraphWin("My Circle", 500, 500)
drawHouse(win, "yellow")
'''

