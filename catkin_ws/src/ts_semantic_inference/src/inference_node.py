#!/usr/bin/env python

import rospy

if __name__ == '__main__':
    rospy.init_node('inference_node')
    
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        rospy.loginfo("Hello World!")
        rate.sleep()