rotation = 13
textFile = open("test.txt", "r")

def rotateLetter(letter):
  numericLetter = ord(letter) - 97
  numericLetter += rotation
  numericLetter = numericLetter%26
  numericLetter += 97
  encodedLetter = chr(numericLetter)
  return encodedLetter



for lines in textFile:
  lowerCaseLines = lines.lower()
  for letter in lowerCaseLines:

    isLetter = (ord(letter) >= 97) and (ord(letter) <= 122)
    
    if (isLetter):
      encodedLetter = rotateLetter(letter)
      print(encodedLetter, end = '')
    else:
      print(letter, end='')
      
      
    
textFile.close()




