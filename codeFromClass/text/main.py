textFile = open("test.txt", "r")
for lines in textFile:
  lowerCaseLines = lines.lower()
  for letter in lowerCaseLines:
    
    print(ord(letter)-97, end = '')
textFile.close()

