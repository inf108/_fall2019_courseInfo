from graphics import *

#(win, 75)
def dalekTop(win, x, y, size):
  radius = size
  domeColor = "grey"
  bodyColor = "grey"
  
  c = Circle(Point(x,y), radius)
  c.setFill(domeColor)
  c.draw(win)

  topLeftX = x - radius
  topLeftY = y
  bottomRightX = x + radius
  bottomRightY = y + radius
  
  r = Rectangle(Point(topLeftX, topLeftY), Point(bottomRightX, bottomRightY))
  r.setFill(bodyColor)
  r.draw(win)

def dalekBottom(win, x, y, size):
  top = y
  bottom = y + size*3
  topL = x - size
  topR = x + size
  bottomL = x - 2 * size
  bottomR = x + 1.55 * size

  p = Polygon(Point(topL, top), Point(topR, top), Point(bottomR, bottom), Point(bottomL, bottom))
  p.setFill("grey")
  p.draw(win)


def main():
  win = GraphWin("Dalek", 500, 1000)
  
  dalekX = 250
  dalekY = 150
  size = 75
  dalekTop(win, dalekX, dalekY, size)

  dalekBottom(win, dalekX, dalekY + size, size)
  win.getMouse() # Pause to view result
  win.close()    # Close window when done

main()
