# Follow along in the team repository
# in YOUR folder & your branch

from graphics import *


#define main function
def main():
    win = GraphWin("My Circle", 500, 500)
    
    circle = Circle(Point(250,250), 100)
    circle.draw(win)
    

    drawRectangle(win, Point(0,0), Point(40,30), "red")
    drawRectangle(win, Point(40,27), Point(56,39), "blue")
    drawRectangle(win, Point(200,400), Point(266,412), "green")
    
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

#use main function
main()
