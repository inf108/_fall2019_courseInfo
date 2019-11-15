from graphics import *

def main():
    win = GraphWin("Dalek", 300, 500)
    
    c = Circle(Point(50,50), 10)
    c.draw(win)

    r = Rectangle(Point(25, 25), Point(75, 75))
    r.draw(win)


    
    win.getMouse() # Pause to view result
    win.close()    # Close window when done

main()
