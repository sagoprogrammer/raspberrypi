import RPi.GPIO as GPIO

red=19
blue=12
green=13
GPIO.setmode(GPIO.BCM)


GPIO.setup(red, GPIO.OUT)
GPIO.setup(blue, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

p=GPIO.PWM(red, 1000)
b=GPIO.PWM(blue, 1000)
g=GPIO.PWM(green, 1000)

p.start(100)
b.start(100)
g.start(100)
i=None
try: 
   while i!='q':

    try:
       
       d=input("set red color brightness:")
       e=input("set blue color brightness :")
       f=input("set green color brightness:")

       if (d=='q'):
         break;
       #p.ChangeFrequency(int(f)) 
       p.ChangeDutyCycle(int(d))
       b.ChangeDutyCycle(int(e))
       g.ChangeDutyCycle(int(f))

    except ValueError as e:
        pass
except KeyboardInterrupt as e:
    print("Recived Ctrl+C -> Quitting...")
    pass          	
GPIO.stop()
GPIO.cleanup()