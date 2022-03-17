import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
PIR_PIN = 4 # Assign GPIO4 pin 7 to PIR
GPIO.setup(PIR_PIN, GPIO.IN) # Setup GPIO pin PIRas inputprint('Sensorinitializing . . .')
time.sleep(60) # Give sensor time to start-up, 60secondsprint('Active')

def pir(pin):
    print('Motion Detected!')

GPIO.add_event_detect(4, GPIO.FALLING,callback=pir,bouncetime=100)

print('[Press Ctrl + C to end program!]')
try:
        while True:
            time.sleep(0.001)
            
except KeyboardInterrupt:
                print('\nScript ended')
                
finally:GPIO.cleanup()