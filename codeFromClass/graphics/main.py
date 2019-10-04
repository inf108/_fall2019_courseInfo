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

#define main function
def main():
    win = GraphWin("My Circle", 500, 500)
    
    circle = Circle(Point(250,250), 100)
    circle.draw(win)
    
    pointA = Point(10,20)
    pointB = pointOffset(pointA, 50, 50)
    drawRectangle(win, pointA, pointB, "yellow")

    drawRectangle(win, Point(0,0), Point(40,30), "red")
    drawRectangle(win, Point(40,27), Point(56,39), "blue")
    drawRectangle(win, Point(200,400), Point(266,412), "green")
    
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

#use main function
main()
