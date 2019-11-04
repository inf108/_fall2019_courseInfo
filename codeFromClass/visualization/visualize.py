filename = "forestfires.csv"
forestFireData = open(filename, 'r')


for line in forestFireData:
  print(line.split(','))

print(forestFireData.readline())
