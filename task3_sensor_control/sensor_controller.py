#try:
#    from .fake_gpio import GPIO # For running app
#except ImportError:
#    from fake_gpio import GPIO # For running main
import RPi.GPIO as GPIO # For testing in Raspberry Pi
# import ...
import time

class SensorController:

  def __init__(self):
    self.PIN_TRIGGER = 18 # do not change
    self.PIN_ECHO = 24 # do not change
    self.distance = None
    self.color_from_distance = [False, False, False]
    print('Sensor controller initiated')

  def track_rod(self):
    print('Monitoring')
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(self.PIN_TRIGGER, GPIO.OUT) # setting up trigger pin as output 
    GPIO.setup(self.PIN_ECHO, GPIO.IN) # echo pin as input
    observations = []
    #first off, rest for some time, now start the burst, takes rest, Stop it again  
    for i in range(20):

      GPIO.output(self.PIN_TRIGGER, False)
      time.sleep(0.2)          
      GPIO.output(self.PIN_TRIGGER, True)
      time.sleep(0.2)
      GPIO.output(self.PIN_TRIGGER, False)
      # finding the duration of wave burst
      while GPIO.input(self.PIN_ECHO) == False:
        start_time = time.time() 
        #print("----start time {}-----".format(start_time))
      while GPIO.input(self.PIN_ECHO) == True:
        end_time = time.time()
        #print("----end time {}-----".format(end_time))
      duration = end_time - start_time #time in seconds
      #print("----Duration {}-----".format(duration))
      #to calculate distnce in cms 
      c_distance = (34300*duration)/2 
       
      observations.append(round(c_distance))

    print("observations List:\n", observations)
    observations.sort()
    median_distance = (observations[9]+observations[10])/2
    print("observations List after sorting:\n", observations)
    print("Median Distance:", median_distance)
    #print("Distance: {} cm".format(c_distance))
    self.distance = round(median_distance)

    if(self.distance >=4 and self.distance <=9): # in yellow
      self.color_from_distance = [False, False, True]
    elif(self.distance >=9 and self.distance <=14): # in purple
      self.color_from_distance = [False, True, False]
    elif(self.distance >=14 and self.distance <=19): # in green
      self.color_from_distance = [True, False, False]
    elif(self.distance >=4 and self.distance <=14): # in between yellow and purple
      self.color_from_distance = [False, True, True]
    elif(self.distance >=9 and self.distance <=19): # in between Green and purple
      self.color_from_distance = [True, True, False]
    else:
      print("find the problem\n")
      self.color_from_distance= [False, False, False]   

    GPIO.cleanup()

  def get_distance(self):
    return self.distance

  def get_color_from_distance(self):
    return self.color_from_distance 