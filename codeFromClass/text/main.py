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
    encodedLetter = rotateLetter(letter)
    print(encodedLetter, end = '')
textFile.close()

print()
