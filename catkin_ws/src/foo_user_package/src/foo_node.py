#!/usr/bin/env python

import cv2
import rospy
import rospkg
rospack = rospkg.RosPack()

from ts_semantic_inference.srv import SemanticInference, SemanticInferenceResponse
from cv_bridge import CvBridge

image_name = "scene00555.jpg"

def semantic_inference_client(input_image):
    bridge = CvBridge()

    rospy.wait_for_service('semantic_inference')
    try:
        semantic_inference = rospy.ServiceProxy('semantic_inference', SemanticInference)
        response = semantic_inference(bridge.cv2_to_imgmsg(input_image, encoding="passthrough"))
        return bridge.imgmsg_to_cv2(response.output, desired_encoding='passthrough')
    except rospy.ServiceException as e:
        print("Service call failed: %s"%e)

if __name__ == '__main__':
    rospy.init_node('foo_node')

    image_file = rospack.get_path("foo_user_package") + "/images/" + image_name
    print(image_file)
    image = cv2.imread(image_file)
    result_image = semantic_inference_client(image)

    cv2.imshow('', result_image)
    if cv2.waitKey(0) & 0xFF == ord('q'):
        cv2.destroyAllWindows()