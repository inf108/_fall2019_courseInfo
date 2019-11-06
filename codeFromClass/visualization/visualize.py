from graphics import *
import math

filename = "forestfires.csv"
xyScale = 100
columnsToUse = ['X', 'Y', 'month', 'day', 'temp', 'RH', 'wind', 'rain', 'area']
radiusMultiplier = 2

def cleanString(myString):
  newString = ""
  for letter in myString:
    if (letter != "\n"):
      newString += letter
  return newString

def cleanList(myList):
  for i in range(len(myList)):
    myList[i] = cleanString(myList[i])
  return myList
    

forestFireData = open(filename, 'r')

columnHeadings = forestFireData.readline().split(',')
columnHeadings = cleanList(columnHeadings)

rowsOfFireData = []

for line in forestFireData:
  currentRow = {}
  currentRowAsList = line.split(',')
  currentRowAsList = cleanList(currentRowAsList)

  for i in range(len(currentRowAsList)): 
    currentRow[columnHeadings[i]] = currentRowAsList[i]
  #print(currentRow)
  rowsOfFireData.append(currentRow)

win = GraphWin("Forest Fires", 900, 900)

for fire in rowsOfFireData:
  x = float(fire["X"]) * xyScale - xyScale/2
  y = float(fire["Y"]) * xyScale - xyScale/2
  radius = math.sqrt(float(fire["area"])/math.pi) * radiusMultiplier
  drawnFire = Circle(Point(x, y), radius)
  #drawnFire.setFill("grey")
  #drawnFire.setOutline("grey")
  drawnFire.draw(win)
  
  
win.getMouse() # Pause to view result
win.close()    # Close window when done

