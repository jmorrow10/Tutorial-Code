#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int64


def start():
    rospy.init_node('talk')

    #create variables, pubs, and subs here

    pubToListener = rospy.Publisher('NUMS', Int64, queue_size=10)

    global num
    num = 0

    rate = rospy.Rate(10) #10hz

    while not rospy.is_shutdown():
        #do some stuff
        num = num + 1

        pubToListener.publish(num)

        rate.sleep()

    rospy.spin()

if __name__ == '__main__':
    start()