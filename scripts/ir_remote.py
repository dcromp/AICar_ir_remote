#!/usr/bin/env python

import rospy
from std_msgs.msg import String
import RPi.GPIO as GPIO

class InfraRedRemote(object):
    def __init__(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(IR,GPIO.IN)
        IR = 17
        n=0
        self.action_pub = rospy.Publisher('action', String, queue_size=1)
        self.action_pub.publish("stop")
        self.loop()

        def loop(self):
            rate = rospy.Rate(30)
            while not rospy.is_shutdown():
                key = self.getkey()
                if(key != None):
                    n = 0
                    if key == 0x18:
                        self.action_pub.publish("foward")
                    if key == 0x08:
                        self.action_pub.publish("left")
                    if key == 0x1c:
                        self.action_pub.publish("stop")
                    if key == 0x5a:
                        self.action_pub.publish("right")
                    if key == 0x52:
                        self.action_pub.publish("backward")
                else:
                    n += 1
                    if n > 20000:
                        n = 0
                        self.action_pub.publish("stop")
            rate.sleep()

    def getkey(self):
        if GPIO.input(IR) == 0:
            count = 0
            while GPIO.input(IR) == 0 and count < 200:  #9ms
                count += 1
                time.sleep(0.00006)
            if(count < 10):
    			return;
    		count = 0
            while GPIO.input(IR) == 1 and count < 80:  #4.5ms
    			count += 1
    			time.sleep(0.00006)
    		idx = 0
    		cnt = 0
    		data = [0,0,0,0]
            for i in range(0,32):
    			count = 0
                while GPIO.input(IR) == 0 and count < 15:    #0.56ms
    				count += 1
    				time.sleep(0.00006)
    			count = 0
                while GPIO.input(IR) == 1 and count < 40:   #0: 0.56mx
    				count += 1                               #1: 1.69ms
    				time.sleep(0.00006)
                if count > 7:
    				data[idx] |= 1<<cnt
                if cnt == 7:
    				cnt = 0
    				idx += 1
                else:
    				cnt += 1
    		if data[0]+data[1] == 0xFF and data[2]+data[3] == 0xFF:  #check
    			return data[2]
    		else:
                pass

if __name__ == '__main__':
    try:
        rospy.init_node('ir_remote')
        InfraRedRemote()
    except rospy.ROSInterruptException:
        rospy.logerr('Could not start InfraRedRemote node.')
        GPIO.cleanup()
