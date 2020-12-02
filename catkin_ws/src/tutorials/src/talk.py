#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int64


def start():
    rospy.init_node('talk.py')

    #create vars pubs and subs
    pubTosub = rospy.Publisher('NUM', Int64, queue_size = 10)

    global num
    num = 0

    rate = rospy.Rate(10) #10 hz

    while not rospy.is_shutdown():
        #do some stuff
        
        pubTosub.publish(num)
        num = num + 1


        rate.sleep()

    rospy.spin()



if __name__ == '__main__':
    start()