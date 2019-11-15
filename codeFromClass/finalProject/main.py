from graphics import *

#(win, 75)
def dalekTop(win, size):
  x = 150
  y = 150
  radius = size
  domeColor = "grey"
  bodyColor = "grey"
  
  c = Circle(Point(x,y), radius)
  c.setFill(domeColor)
  c.draw(win)

  topLeftX = x - radius
  topLeftY = y
  bottomRightX = x + radius
  bottomRightY = y + 2*radius
  
  r = Rectangle(Point(topLeftX, topLeftY), Point(bottomRightX, bottomRightY))
  r.setFill(bodyColor)
  r.draw(win)


def main():
  win = GraphWin("Dalek", 300, 500)

  dalekTop(win, 75)

  


  
  win.getMouse() # Pause to view result
  win.close()    # Close window when done

main()
