# Follow along in the team repository
# in YOUR folder & your branch

from graphics import *
from house import *
from roof import *

#define main function
def main():
    win = GraphWin("My House", 500, 500)

    entry = Entry(Point(250,480), 20)
    entry.draw(win)

    for i in range(20):
        drawRandomCloud(win)

    win.getKey()
    colorChoice = entry.getText()
    if (colorChoice == "y"):
        colorName = "yellow"
    elif(colorChoice == "b"):
        colorName = "blue"
    elif(colorChoice == "p"):
        colorName = "pink"
    elif(colorChoice == "o"):
        colorName = "orange"
    else:
        colorName = "green"
    
    drawHouse(win, colorName)
    drawRoof(win)

    win.getMouse() # Pause to view result
    win.close()    # Close window when done

#use main function
main()
