textFile = open("test.txt", "r")
for lines in textFile:
  lowerCaseLines = lines.lower()
  for letter in lowerCaseLines:
    print(letter)
textFile.close()

