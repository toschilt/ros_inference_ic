#!/usr/bin/env python

import rospy
from inference_submodule import image_detect
from ts_semantic_inference.srv import SemanticInference, SemanticInferenceResponse
from cv_bridge import CvBridge

def handle_semantic_inference(req):
    req_image = req.image

    bridge = CvBridge()
    cv_image = bridge.imgmsg_to_cv2(req_image, desired_encoding='passthrough') 
    
    result_image = image_detect(cv_image) 

    response = SemanticInferenceResponse()
    response.image = bridge.cv2_to_imgmsg(result_image, encoding="passthrough")
    return response

if __name__ == '__main__':
    rospy.init_node('inference_node')
    s = rospy.Service('semantic_inference', SemanticInference, handle_semantic_inference)
    rospy.spin() 