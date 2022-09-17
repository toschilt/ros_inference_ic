#!/usr/bin/env python

import rospy
from inference_submodule import image_detect
from ts_semantic_inference.srv import SemanticInference, SemanticInferenceResponse

def handle_semantic_inference(req):
    image_detect() 

if __name__ == '__main__':
    rospy.init_node('inference_node')
    s = rospy.Service('semantic_inference', SemanticInference, handle_semantic_inference)
    rospy.spin()  