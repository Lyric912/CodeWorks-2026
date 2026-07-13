<<<<<<< Updated upstream
from gpiozero import LED
from time import sleep

#LED PIN ASSIGNMENTS
red = LED(17)
yellow = LED(27)
green = LED(22)

while True:
  #GREEN
  green.on()
  red.off()
  yellow.off()
  sleep(1)
  green.off()
  sleep(5)

  #YELLOW
  yellow.on()
  green.off()
  red.off()
  sleep(3)

  #RED
  green.off()
  red.on()
  yellow.off()
  sleep(5)
=======
from gpiozero import LED
from time import sleep

#LED PIN ASSIGNMENTS   
red = LED(17)
yellow = LED(27)
green = LED(22)

while True:
    #GREEN  
    green.on()
    red.off()
    yellow.off()
    sleep(1)
    green.off()
    sleep(5)

    #YELLOW
    yellow.on()
    green.off()
    red.off()
    sleep(3)

    #RED
    green.off()
    red.on() 
    yellow.off()
    sleep(5)
>>>>>>> Stashed changes
