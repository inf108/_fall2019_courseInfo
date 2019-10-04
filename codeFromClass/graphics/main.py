# Follow along in the team repository
# in YOUR folder & your branch

from graphics import *

def main():
    win = GraphWin("My Circle", 500, 500)
    
    circle = Circle(Point(250,250), 100)
    circle.draw(win)
    
    rectangle = Rectangle(Point(250,250), Point(300,400))
    rectangle.setFill("red")
    rectangle.draw(win)
    
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()
