#!/usr/bin/env python3
import rospy


def start():
    rospy.init_node('annoying_node')

    # declare variables, subscribers, and publishers
    message = 'hi there'

    rate = rospy.Rate(10) #10 hz

    while not rospy.is_shutdown():
        #do some stuff
        print(message)
        rate.sleep()

    rospy.spin()



if __name__ == '__main__':
    start()