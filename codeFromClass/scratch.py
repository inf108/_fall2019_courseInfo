import time

timeLimit = 5
startTime = time.time()
isRunning = True
while isRunning:
  text = input("Type something:")
  print(text)
  isRunning = time.time() - startTime < timeLimit
  


