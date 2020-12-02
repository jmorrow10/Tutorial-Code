#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int64

def callback(data):
    print(data.data)


def start():
    rospy.init_node('listen')

    #create stuff here
    rospy.Subscriber('NUMS', Int64, callback)

    rospy.spin()



if __name__ == '__main__':
    start()