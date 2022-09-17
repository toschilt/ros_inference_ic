#!/usr/bin/env python

import rospy
from ts_semantic_inference import image_detect

def handle_semantic_inference(req):
    print("Do the thing")

if __name__ == '__main__':
    rospy.init_node('inference_node')
    s = rospy.Service('semantic_inference', SemanticInference, handle_semantic_inference)
    rospy.spin()  