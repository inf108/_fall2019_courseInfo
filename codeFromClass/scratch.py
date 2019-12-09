import time

timeLimit = 5
startTime = time.time()
isRunning = True
while isRunning:
  text = input("Type something:")
  print(text)
  elapsedTime = time.time() - startTime
  isRunning = elapsedTime < timeLimit
  print(isRunning)
  


