import cv2
import numpy as np

try:
    from .camera import Camera 
except ImportError:
    from camera import Camera 

# from pi_camera import Camera # For Raspberry Pi

class OpenCVController(object):

    def __init__(self):
        self.current_color = [False,False,False]
        self.camera = Camera()
        print('OpenCV controller initiated')
    
    def process_frame(self):
        frame = self.camera.get_frame()
       
        frame = np.fromstring(frame, np.uint8)
        frame = cv2.imdecode(frame, cv2.COLOR_BGR2RGB) # now frame contains HSV format
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        win1 = "Result window"
        win2 = "Mask window"

        #detecting Yellow Color
        lower_yellow = np.array([35 , 74, 94])
        upper_yellow = np.array([50 , 255, 255])
        #detecting red Color
        lower_red = np.array([140 , 43, 93])
        upper_red = np.array([192 , 255, 255]) 
        
        #lower_red_1= np.array([0,100,20])
        #upper_red_1= np.array([10,255,255])
        #lower_red_2= np.array([160,100,20])
        #upper_red_2= np.array([179,255,255])
        
        
        #detecting green Color
        lower_green = np.array([35 , 74, 94])
        upper_green = np.array([50 , 255, 255]) 
        #detecting purple Color
        lower_purple = np.array([85 , 70, 66])
        upper_purple = np.array([120 , 255, 255])

        #creating masks

        #mask_1=cv2.inRange(hsv, lower_red_1, upper_red_1)
        #mask_2=cv2.inRange(hsv, lower_red_2, upper_red_2)
        #mask_red = mask_1 + mask_2
        mask_red = cv2.inRange(hsv, lower_red, upper_red)
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
        cv2.rectangle(frame,(yel_x,yel_y), (yel_x + y_width , yel_y + y_height),(25, 225, 225), 3 )
        end_yellow= yel_x + y_width
        #print(str(len(y_contours))) #total no of contours 

        #---------------------------finding red contours--------------------------------------
        r_contours ,r_heir = cv2.findContours(mask_red, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
        #cv2.drawContours(frame, r_contours, -1, (0, 0, 255), 3)
        r_area =  max(r_contours, key = cv2.contourArea)
        red_x, red_y, r_width, r_height = cv2.boundingRect(r_area)
        cv2.rectangle(frame,(red_x,red_y), (red_x + r_width , red_y + r_height),(0,0,255), 3 )
        end_red = red_x + r_width
        
        #--------------------------finding purple contours----------------------------------------

        p_contours ,p_heir = cv2.findContours(purple_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
        cv2.drawContours(frame, p_contours, -1, (201, 14, 225), 3)
        p_area =  max(p_contours, key = cv2.contourArea)
        purple_x, purple_y, p_width, p_height = cv2.boundingRect(p_area)
        cv2.rectangle(frame,(purple_x,purple_y), (purple_x + p_width , purple_y + p_height),(201, 14, 225), 5 )
        end_purple = purple_x + p_width
        

        #-------------------------finding green contours------------------------------------------
        g_contours ,g_heir = cv2.findContours(green_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE) 
        #cv2.drawContours(frame, g_contours, -1, (0, 255, 0), 3)
        g_area =  max(g_contours, key = cv2.contourArea)
        green_x, green_y, g_width, g_height = cv2.boundingRect(g_area)
        cv2.rectangle(frame,(green_x,green_y), (green_x + g_width , green_y + g_height),(0,255,0), 5 )
        end_green = green_x + g_width
        
        
        #Now Applying checks
        if (red_x > green_x and end_red < end_green) or (end_red < end_green): # red is in green
            self.current_color = [True,False,False]
        elif(red_x > purple_x and end_red < end_purple): # red is in purple
            self.current_color = [False,True,False]
        elif(red_x > yel_x and end_red < end_yellow ): #red is in yellow
            self.current_color = [False,False,True]
        elif(red_x > green_x and red_x < purple_x) and (end_red > purple_x and end_red < end_purple)or (end_red > purple_x): # red is in between green and purple
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
        #cv2.waitKey(0) 
        #cv2.destroyAllWindows() 
       
    
        
        
        print('Monitoring')
        return frame

    def get_current_color(self):
        return self.current_color
