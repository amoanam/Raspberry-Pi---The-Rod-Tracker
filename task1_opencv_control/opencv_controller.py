import cv2
import numpy as np


try:
    from .camera import Camera # For running app
except ImportError:
    from camera import Camera # For running main

#from pi_camera import Camera # For Raspberry Pi
#from picamera import PiCamera as Camera

class OpenCVController(object):

    def __init__(self):
        self.current_color = [False,False,False]
        self.camera = Camera()
        print('OpenCV controller initiated')
    
    def process_frame(self):
        frame = self.camera.get_frame()
        '''
        #print("frame in controller start",type(frame))
        frame = np.fromstring(frame, np.uint8)
        frame = cv2.imdecode(frame, cv2.COLOR_BGR2RGB) # now frame contains HSV format
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        win1 = "Result window"
        win2 = "Mask window"

        #detecting Yellow Color
        lower_yellow = np.array([20 , 74, 94])
        upper_yellow = np.array([53 , 255, 255])
        #detecting red Color
        lower_red = np.array([160 , 43, 93])
        upper_red = np.array([190 , 255, 255]) 
        
           
        #detecting green Color
        lower_green = np.array([40 , 74, 94])
        upper_green = np.array([53 , 255, 255]) 
        #detecting purple Color
        lower_purple = np.array([130 , 43, 93])
        upper_purple = np.array([170 , 255, 255])

        #creating masks

        #mask_1=cv2.inRange(frame, lower_red_1, upper_red_1)
        #mask_2=cv2.inRange(hsv, lower_red, upper_red)
        #mask_red = mask_1 + mask_2
        red_mask = cv2.inRange(hsv, lower_red, upper_red)
        yellow_mask = cv2.inRange(frame, lower_yellow, upper_yellow)
        purple_mask = cv2.inRange(hsv, lower_purple, upper_purple)
        green_mask = cv2.inRange(hsv, lower_green, upper_green)

        res = cv2.bitwise_and(frame, frame, mask=yellow_mask)
        #-----------------------finding yellow contours---------------------------------------

        y_contours ,y_heir = cv2.findContours(yellow_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
        #cv2.drawContours(frame, y_contours, -1, (25, 225, 225), 3)
        y_area =  max(y_contours, key = cv2.contourArea)
        #print(y_area)
        yel_x, yel_y, y_width, y_height = cv2.boundingRect(y_area)
        cv2.rectangle(frame, (yel_x, yel_y-50), (yel_x + 100, yel_y  ), (25,225,255), -1)
        cv2.putText(frame,"Yellow",(yel_x, yel_y-15),cv2.FONT_HERSHEY_DUPLEX,1.0,(255,255,255),2)
        cv2.rectangle(frame,(yel_x,yel_y), (yel_x + y_width , yel_y + y_height),(25, 225, 225), 3 )
        
        end_yellow= yel_x + y_width
        #print(str(len(y_contours))) #total no of contours 

        #---------------------------finding red contours--------------------------------------
        r_contours ,r_heir = cv2.findContours(red_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
        #cv2.drawContours(frame, r_contours, -1, (0, 0, 255), 3)
        r_area =  max(r_contours, key = cv2.contourArea)
        red_x, red_y, r_width, r_height = cv2.boundingRect(r_area)
        cv2.rectangle(frame, (red_x, red_y-50), (red_x + 100, red_y  ), (0,0,255), -1)
        cv2.putText(frame,"Mark",(red_x, red_y-15),cv2.FONT_HERSHEY_DUPLEX,1.0,(255,255,255),2)
        cv2.rectangle(frame,(red_x,red_y), (red_x + r_width , red_y + r_height),(0,0,255), 3 )
        end_red = red_x + r_width
        
        #--------------------------finding purple contours----------------------------------------

        p_contours ,p_heir = cv2.findContours(purple_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
        #cv2.drawContours(frame, p_contours, -1, (201, 14, 225), 3)
        p_area =  max(p_contours, key = cv2.contourArea)
        purple_x, purple_y, p_width, p_height = cv2.boundingRect(p_area)
        cv2.rectangle(frame, (purple_x, purple_y-50), (purple_x + 100, purple_y  ), (201,14,255), -1)
        cv2.putText(frame,"Purple",(purple_x, purple_y-15),cv2.FONT_HERSHEY_DUPLEX,1.0,(255,255,255),2)
        cv2.rectangle(frame,(purple_x,purple_y), (purple_x + p_width , purple_y + p_height),(201, 14, 225), 5 )
        end_purple = purple_x + p_width
        

        #-------------------------finding green contours------------------------------------------
        g_contours ,g_heir = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
        #cv2.drawContours(frame, g_contours, -1, (0, 255, 0), 3)
        g_area =  max(g_contours, key = cv2.contourArea)
        green_x, green_y, g_width, g_height = cv2.boundingRect(g_area)
        cv2.rectangle(frame, (green_x, green_y-50), (green_x + 100, green_y  ), (0,225,0), -1)
        cv2.putText(frame,"Green",(green_x, green_y-15),cv2.FONT_HERSHEY_DUPLEX,1.0,(255,255,255),2)
        cv2.rectangle(frame,(green_x,green_y), (green_x + g_width , green_y + g_height),(0,255,0), 5 )
        end_green = green_x + g_width
        
        
        #Now Applying checks
        if (red_x > green_x and end_red < end_green) or (end_red < end_green): # red is in green
            self.current_color = [True,False,False]
        elif(red_x > purple_x and end_red < end_purple): # red is in purple
            self.current_color = [False,True,False]
        elif(red_x > yel_x and end_red < end_yellow ): #red is in yellow
            self.current_color = [False,False,True]
        elif(red_x > green_x and red_x < purple_x) and (end_red > purple_x and end_red < end_purple): # red is in between green and purple
            self.current_color = [True,True,False]
        elif(red_x > purple_x and red_x < yel_x) and (end_red > yel_x and end_red < end_yellow): # red is in between purple and Yellow
            self.current_color = [False,True,True]
        else:
            print("find the problem !")
        
        
        #cv2.namedWindow(win1)
        #cv2.namedWindow(win2)
        #cv2.moveWindow(win1, 40,30)  # Move it to (40,30)
        #cv2.moveWindow(win2, 40,300)  # Move it to (10,300)
        #cv2.imshow(win1,res)
        cv2.namedWindow("HSV")   # del after sucess
        cv2.moveWindow("HSV", 100,241) # del after successs
        hsv = cv2.resize(hsv, (480, 270))
        cv2.imshow("HSV",hsv)
        #cv2.imshow(win2,yellow_mask)
        
        #frame= frame.tobytes('A')
        #print("frame in controller end",type(frame))
        print('Monitoring')
        '''
        return frame

    def get_current_color(self):
        return self.current_color
