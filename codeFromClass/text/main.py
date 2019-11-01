rotation = 13
inTextFile = open("test.txt", "r")
outTextFile = open("out.txt", "w")

def rotateLetter(letter):
  numericLetter = ord(letter) - 97
  numericLetter += rotation
  numericLetter = numericLetter%26
  numericLetter += 97
  encodedLetter = chr(numericLetter)
  return encodedLetter

for lines in inTextFile:
  lowerCaseLines = lines.lower()
  encodedLine = ""
  for letter in lowerCaseLines:
    isLetter = (ord(letter) >= 97) and (ord(letter) <= 122)
    if (isLetter):
      encodedLetter = rotateLetter(letter)
      encodedLine += encodedLetter
    else:
      encodedLine += letter
  outTextFile.write(encodedLine)    
    
inTextFile.close()
outTextFile.close()




