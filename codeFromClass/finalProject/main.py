from graphics import *

def createCircle(win, x, y, size, color):
  c = Circle(Point(x,y), size)
  c.setFill(color)
  c.draw(win)
  return c

def createRectangle(win, x, y, size, bodyColor):
  topLeftX = x - size
  topLeftY = y
  bottomRightX = x + size
  bottomRightY = y + size
  
  r = Rectangle(Point(topLeftX, topLeftY), Point(bottomRightX, bottomRightY))
  r.setFill(bodyColor)
  r.draw(win)
  return r

def dalekTop(win, x, y, size):
  domeColor = "grey"
  bodyColor = "grey"
  
  c = createCircle(win, x, y, size, domeColor)
  r = createRectangle(win, x, y, size, bodyColor)

  return [c, r]

def dalekBottom(win, x, y, size):
  top = y
  bottom = y + size*3
  topL = x - size
  topR = x + size
  bottomL = x - 1.55 * size
  bottomR = x + 2 * size

  p = Polygon(Point(topL, top), Point(topR, top), Point(bottomR, bottom), Point(bottomL, bottom))
  p.setFill("grey")
  p.draw(win)

  return [p]

def createDalek(win, x, y, size):
  top = dalekTop(win, x, y, size)
  bottom = dalekBottom(win, x, y + size, size)

  return top + bottom


def main():
  size = 75
  dalekSpeed = 10
  dalekX = 250
  dalekY = 500

  win = GraphWin("Dalek", 1440, 900)

  dalek = createDalek(win, dalekX, dalekY, size)

  while (True):
    
    #print(dalekX)
    
    for part in dalek:
      part.move(dalekSpeed, 0)

    time.sleep(0.1)

  
  win.getMouse() # Pause to view result
  win.close()    # Close window when done

main()
