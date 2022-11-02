starting = False 
while True:
  count = int(input(">").lower())
  if count == "start":
    if starting == True:
      print("The car is already running")
    else:
      starting = True
      print("The car has started running")
  
  elif count == "stop":
    if not starting:
      print("The is already stopped ")
    else:
      starting = False
      print("The car has stopped")
  
  elif count == "quit":
    break
  elif count == "help":
  print("start - to start the car
stop - to stop the car
quit - to end the game
help -  for instructions")
else:
  print("The game has quitted!!!")
