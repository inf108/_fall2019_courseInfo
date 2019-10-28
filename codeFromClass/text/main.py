rotation = 13
textFile = open("test.txt", "r")

for lines in textFile:
  lowerCaseLines = lines.lower()
  for letter in lowerCaseLines:
    numericLetter = ord(letter) - 97
    numericLetter = numericLetter + rotation
    numericLetter = numericLetter%26
    print(numericLetter, end = '')
textFile.close()

