  
from gpiozero import LED
from time import sleep

led = LED(17)
while True:
 on=int(input('light on press 1 off press 2:'))
 if on==1:
   led.on()
   sleep(100000)
   on=int(input('light off press 2:'))
 elif on==2:
   led.off()
   sleep(1)
