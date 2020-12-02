#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int64


def callback(data):
    print(data.data)


def start():
    rospy.init_node('listen.py')

    #create vars pubs and subs

    rospy.Subscriber('NUM', Int64, callback)

    rospy.spin()



if __name__ == '__main__':
    start()