from opencv_controller import OpenCVController
import time
import cv2
import numpy as np
import base64

# Do NOT change this script
opencv_controller = OpenCVController()

for i in range(5):
  print("----------- Distance number: ", i)
  frame = opencv_controller.process_frame()
  #print("frame in main",type(frame))

  # Display in window
  jpg_as_np = np.fromstring(frame, np.uint8)
  img = cv2.imdecode(jpg_as_np, cv2.COLOR_BGR2RGB)
  cv2.namedWindow("image")
  cv2.moveWindow("image", 600,241)
  frame = cv2.resize(frame, (480, 270)) # not in raspberry pi
  cv2.imshow('image', frame) # Not in Raspberry Pi
  cv2.resizeWindow('image', 100, 100)
  print("Current color from OpenCV: ", opencv_controller.get_current_color())
  print("---------------------------------")
  
  cv2.waitKey(0) # Not in Raspberry Pi
  cv2.destroyAllWindows() # Not in Raspberry Pi

