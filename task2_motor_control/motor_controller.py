#try:
#    from .fake_gpio import GPIO # For running app
#except ImportError:
#    from fake_gpio import GPIO # For running main
import RPi.GPIO as GPIO # For testing in Raspberry Pi
import random
from time import sleep

class MotorController(object):

  def __init__(self):
    self.working = False
    self.status = "Motor Status"

  def start_motor(self):
    print(self.working)
    while(self.working == True):
      print('Motor started')
      self.PIN_STEP = 25 # do not change
      self.PIN_DIR = 8 # do not change
      self.working = True
      orientation = [0,1]
      angle = [270, 90]
      random_orientation = random.choice(orientation) 
      random_angle = random.choice(angle)
      print(random_orientation)
      print(random_angle)

      steps_90 = 400 # i.e., 90/0.255
      steps_270 = 1200 # i.e., 270/0.255
      delay = 0.00625 # if we have to complete rotation in 1 sec --> 1/1600(no of steps to make a 360 rotation)
      GPIO.setmode(GPIO.BCM)
      GPIO.setup(self.PIN_STEP, GPIO.OUT)
      GPIO.setup(self.PIN_DIR, GPIO.OUT)

      
      if(random_angle == 90 and random_orientation == 1): # 90 degree in clockwise direction
        self.working = True
        self.status = "motor is rotating 90 degree in clockwise Direction"
        print(self.status ,random_angle, random_orientation )
        for x in range(steps_90):
          GPIO.output(self.PIN_DIR, random_orientation )
          GPIO.output(self.PIN_STEP, GPIO.HIGH)
          sleep(delay) 
          GPIO.output(self.PIN_STEP, GPIO.LOW)
          sleep(delay)
          print(x)

      elif(random_angle == 90 and random_orientation == 0): # 90 degree in Anti-clockwise direction
        self.working = True
        self.status = "motor is rotating 90 degree in Anti-clockwise Direction"
        print(self.status,random_angle, random_orientation)
        for x in range(steps_90):
          GPIO.output(self.PIN_DIR, random_orientation )
          GPIO.output(self.PIN_STEP, GPIO.HIGH)
          sleep(delay) 
          GPIO.output(self.PIN_STEP, GPIO.LOW)
          sleep(delay)
          print(x)

      elif(random_angle == 270 and random_orientation == 1): # 270 degree in clockwise direction
        self.working = True
        self.status = "motor is rotating 270 degree in clockwise Direction" 
        print(self.status ,random_angle, random_orientation)
        for x in range(steps_270):
          GPIO.output(self.PIN_DIR, random_orientation )
          GPIO.output(self.PIN_STEP, GPIO.HIGH)
          sleep(delay) 
          GPIO.output(self.PIN_STEP, GPIO.LOW)
          sleep(delay)
          print(x)

      elif(random_angle == 270 and random_orientation == 0): # 270 degree in Anti-clockwise direction
        self.working = True
        self.status = "motor is rotating 270 degree in Anti-clockwise Direction"
        print(self.status,random_angle, random_orientation)
        for x in range(steps_270):
          GPIO.output(self.PIN_DIR, random_orientation )
          GPIO.output(self.PIN_STEP, GPIO.HIGH)
          sleep(delay) 
          GPIO.output(self.PIN_STEP, GPIO.LOW)
          sleep(delay)
          print(x)
      else:
        self.working = False
  
  def next_color_zone(self):
    print('moving to next color zone')
    self.PIN_STEP = 25 # do not change
    self.PIN_DIR = 8 # do not change
    self.working = True
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.PIN_STEP, GPIO.OUT)
    GPIO.setup(self.PIN_DIR, GPIO.OUT)
    delay = 0.00625
    self.status = "motor is rotating to next color zone"
    for x in range(400):
      GPIO.output(self.PIN_DIR, 1 )
      GPIO.output(self.PIN_STEP, GPIO.HIGH)
      sleep(delay) 
      GPIO.output(self.PIN_STEP, GPIO.LOW)
      sleep(delay)
      print(x)


  def get_status(self):
    return self.status
    
  def is_working(self):
    return self.working
