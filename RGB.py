from ctypes.wintypes import RGB
import time
import RPi.GPIO as GPIO

class RGBA():
       def __init__(self,r,g,b):
              GPIO.setmode(GPIO.BCM)
              channel=[r,g,b]
              for c in channel:
                     GPIO.setup(c,GPIO.OUT)
              self.r=GPIO.PWM(r,60)
              self.g=GPIO.PWM(g,60)       
              self.b=GPIO.PWM(b,60)  
              self.r.start(0)
              self.g.start(0)
              self.b.start(0)     
       def setcolor(self,r,g,b):
              r=100-(r/255)*100
              g=100-(g/255)*100
              b=100-(b/255)*100
              self.r.ChangeDutyCycle(r)
              self.g.ChangeDutyCycle(g)
              self.b.ChangeDutyCycle(b)

#transction colors
led=RGBA(12,13,19)
r=250
g=255
b=10
i=1000
for i in range(700):     
       time.sleep(0.2)  
       e=led.setcolor(r,g,b)      
       print(r,g,b)
       r=r-2
       g=g-4
       b=b+2    
#time.sleep(3)
GPIO.cleanup()              
              
              

              
              




              