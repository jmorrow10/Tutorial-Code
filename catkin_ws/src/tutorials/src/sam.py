#!/usr/bin/env python3
import rospy


def start():
    rospy.init_node('sam.py')

    #create vars pubs and subs

    rate = rospy.Rate(10) #10 hz

    while not rospy.is_shutdown():
        #do some stuff
        print('I know how to code!')
        rate.sleep()

    rospy.spin()



if __name__ == '__main__':
    start()