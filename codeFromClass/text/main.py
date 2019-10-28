rotation = 13
textFile = open("test.txt", "r")

for lines in textFile:
  lowerCaseLines = lines.lower()
  for letter in lowerCaseLines:
    numericLetter = ord(letter) - 97
    print(numericLetter)
    numericLetter = numericLetter + rotation
    print(numericLetter)
    numericLetter = numericLetter%26
    print(numericLetter)
    encodedLetter = chr(numericLetter)
    print(encodedLetter, end = '')
textFile.close()

