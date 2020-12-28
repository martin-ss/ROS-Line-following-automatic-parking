#!/usr/bin/env python
import rospy
import cv2
import numpy as np


def converter_rgb_hsv(blue,green,red):
    rospy.init_node('line_following_node', anonymous=True)
    yellow = np.uint8([[[ blue,green,red ]]])
    hsv_yellow = cv2.cvtColor(yellow,cv2.COLOR_BGR2HSV)
    print( hsv_yellow )

if __name__ == '__main__':
    
    red = int(raw_input("RGB, Red="))
    green = int(raw_input("RGB, Green="))
    blue = int(raw_input("RGB, Blue="))
    converter_rgb_hsv(blue,green,red)