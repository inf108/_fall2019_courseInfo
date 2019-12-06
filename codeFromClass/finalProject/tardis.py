'''
This library contains all the functions necessary to draw a Tardis.
It requires the graphics.py library, which must be in the program's path.

Example of use:

win = GraphWin("Tardis", 500, 800)
createTardis(win, 100, 100, 300)
win.getMouse() # Pause to view result
win.close()    # Close window when done

Exercise:
Criticize this code. 

0. We'll fix the bugs in class before we start the exercise. This might
happen the day before the exercise. It might happen the same day due
to the snow emergency.

1. One person: copy this into your team repository and put in a folder 
that has graphics.py in it.

2. Take turns driving. 

We will have to play this by ear a bit. Each of you will get 5-10 minutes 
to checkout and edit this file, depending on team size, how long step 0 takes,
and whether or not there is a snow cancellation. Remember to leave time to 
commit, push, and for the next team member to pull.

If you find you can't make comments as fast as team members find problems,
multiple people can edit in their own branch at the same time if someone
on your team is comfortable enough with merging a file edited by multiple
people at once using visual studio code's merge functionality.

3. Add comments throughout the code. Use # for single-line comments. 
Criticize this code. Find as many problems as you can. Do this as a group.
Everyone on the team should be looking for things to add to the comments
while the others add them to the comments.

(c) 2019 Cristyn Magnus
This code is for educational purposes only. It can be shared and remixed for 
non-commercial, educational purposes with attribution as long as this entire 
comment text is included. 
Please don't use this code as-is for anything important, as it deliberately sucks.
It is intended as a platform for discussing common coding mistakes and
stylistic failures.
'''

from graphics import *

def createTardis(win, x, y, size):
  panelBlue = color_rgb(50, 50, 100)
  trimBlue = color_rgb(30, 30, 80)
  structureBlue = color_rgb(40, 40,90)
  lightColor = color_rgb(255, 255, 200)

  structure = Rectangle(Point(x, y), Point(x+size, y+size*2))
  structure.setFill(structureBlue)
  structure.draw(win)

  top = Rectangle(Point(x+size*0.05, y-size*0.05), Point(x+size*0.95, y))
  top.setFill(trimBlue)
  top.draw(win)

  bottom = Rectangle(Point(x-size*0.05, y+size*2-size*0.05), Point(x+size*0.05+size, y+size*2))
  bottom.setFill(trimBlue)
  bottom.draw(win)
  
  top2 = Polygon(Point(x+size*0.05, y-size*0.05), Point(x+size*0.45,y-size*0.1), Point(x+size*0.55, y-size*0.1), Point(x+size*0.95, y-size*0.05))
  top2.setFill(trimBlue)
  top2.draw(win)

  topLight = Rectangle(Point(x+size*0.45,y-size*0.1), Point(x+size*0.55, y-size*0.2))
  topLight.setFill(lightColor)
  topLight.setOutline(trimBlue)
  topLight.draw(win)

  topOfLightPoints = []
  topOfLightPoints.append(Point(x+size*0.44,y-size*0.2))
  topOfLightPoints.append(Point(x+size*0.56, y-size*0.2))
  topOfLightPoints.append(Point(x+size*0.5, y-size*0.23))
  
  topOfLight = Polygon(topOfLightPoints)
  topOfLight.setFill(trimBlue)
  topOfLight.draw(win)
  
  x1 = x + size * 0.05 
  x2 = x + size * 0.55
  panelWidth = size * 0.4
  y0 = y + size * 0.06
  y0Height = 0.17 * size + 0.02
  panelGap = 3
  panelHeight = size * 0.4
  y1 = y + size * 0.05 + y0Height
  y2 = y1 + panelGap*2 + panelHeight + 1
  y3 = y2 + panelGap*3 + panelHeight + 1
  y4 = y3 + panelGap*4 + panelHeight + 1
  y5 = y4 + panelGap*5 + panelHeight
  
  doorLine = Line(Point(x + size/2, y0), Point(x + size/2, y + size*2))
  doorLine.draw(win)

  panels = []
  panels.append(Rectangle(Point(x1, y0), Point(x2 + panelWidth, y0 + y0Height - 0.02*size)))
  panels.append(Rectangle(Point(x1, y1), Point(x1 + panelWidth, y1 + panelHeight)))
  panels.append(Rectangle(Point(x2, y1), Point(x2 + panelWidth, y1 + panelHeight)))
  panels.append(Rectangle(Point(x1, y2), Point(x1 + panelWidth, y2 + panelHeight)))
  panels.append(Rectangle(Point(x2, y2), Point(x2 + panelWidth, y2 + panelHeight)))
  panels.append(Rectangle(Point(x1, y3), Point(x1 + panelWidth, y3 + panelHeight)))
  panels.append(Rectangle(Point(x2, y3), Point(x2 + panelWidth, y3 + panelHeight)))
  panels.append(Rectangle(Point(x1, y4), Point(x1 + panelWidth, y4 + panelHeight)))
  panels.append(Rectangle(Point(x2, y4), Point(x2 + panelWidth, y4 + panelHeight)))
  panels.append(Rectangle(Point(x1+0.05*size, y2+0.05*size), Point(x1 + panelWidth - 0.05*size, y2 + panelHeight - 0.05*size)))

  
  windowPanes = []
  windowPanes.append(Line(Point(x1, y1 + panelHeight*0.5), Point(x1+panelWidth, y1 + panelHeight*0.5)))
  windowPanes.append(Line(Point(x2, y1 + panelHeight*0.5), Point(x2+panelWidth, y1 + panelHeight*0.5)))
  windowPanes.append(Line(Point(x1 + panelWidth*0.33, y1), Point(x1 + panelWidth*0.33, y1 + panelHeight)))
  windowPanes.append(Line(Point(x2 + panelWidth*0.33, y1), Point(x2 + panelWidth*0.33, y1 + panelHeight)))
  windowPanes.append(Line(Point(x1 + panelWidth*0.64, y1), Point(x1 + panelWidth*0.64, y1 + panelHeight)))
  windowPanes.append(Line(Point(x2 + panelWidth*0.64, y1), Point(x2 + panelWidth*0.64, y1 + panelHeight)))
  
  for panel in panels:
    panel.setFill(panelBlue)
  
  panels[0].setFill(color_rgb(20,20,70))
  panels[1].setFill(color_rgb(255,255,230))
  panels[1].setOutline(trimBlue)
  panels[1].setWidth(2)
  panels[2].setFill(color_rgb(255,255,230))
  panels[2].setOutline(trimBlue)
  panels[2].setWidth(2)
  panels[-1].setFill(color_rgb(230, 230, 200))

  
  for panel in panels:
    panel.draw(win)
    
  
  topSign = []
  
  for i in range(3):
    topSign.append(Text(panels[0].getCenter(), ""))
                   
  
  topSign[0].setText("POLICE            BOX")
  topSign[1].setText("PUBLIC") 
  topSign[1].move(17,5)
  topSign[2].setText("CALL")
  topSign[2].move(17,-5)

  topSign[0].setSize(26)
  topSign[1].setSize(11)
  topSign[2].setSize(11)

  for text in topSign:
    text.setTextColor("white")
    text.draw(win)
    print(text)

  for item in windowPanes:
    item.setOutline(trimBlue)
    item.setWidth(2)
    item.draw(win)

  doorSign = []
  doorSign.append(Text(panels[-1].getCenter(), "POLICE TELEPHONE"))
  doorSign.append(Text(panels[-1].getCenter(), "FREE"))
  doorSign.append(Text(panels[-1].getCenter(), "FOR USE OF"))
  doorSign.append(Text(panels[-1].getCenter(), "PUBLIC"))
  doorSign.append(Text(panels[-1].getCenter(), "ADVICE & ASSISTANCE"))
  doorSign.append(Text(panels[-1].getCenter(), "OBTAINABLE IMMEDIATELY"))
  doorSign.append(Text(panels[-1].getCenter(), "OFFICERS & CARS"))
  doorSign.append(Text(panels[-1].getCenter(), "RESPOND TO ALL CALLS"))
  doorSign.append(Text(panels[-1].getCenter(), "PULL TO OPEN"))

  dy = panelHeight - size*0.1
  dy = dy/9*0.9
  for i in range(len(doorSign)):
    doorSign[i].setSize(5)
    doorSign[i].move(0, dy*i - (panelHeight-size*0.1)/2 + dy)
    doorSign[i].draw(win)
  
'''
win = GraphWin("Tardis", 500, 800)
createTardis(win, 100, 100, 300)
win.getMouse() # Pause to view result
win.close()    # Close window when done
'''

