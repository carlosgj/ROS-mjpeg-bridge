#!/usr/bin/env python
from __future__ import print_function

import roslib
#roslib.load_manifest('my_package')
import sys
import rospy
import cv2
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def main(args):

    rospy.init_node('image_converter', anonymous=True)
    image_pub = rospy.Publisher("image_topic_2",Image)
    cap = cv2.VideoCapture('http://10.6.96.23:8000/stream.mjpg')
    bridge = CvBridge()

    #oldTime = None
    try:
        while(cap.isOpened() and not rospy.is_shutdown()):
            ret, frame = cap.read()

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

            #newTime = time.time()
            #if oldTime:
                #delta = newTime-oldTime
                #print 1./delta

            #else:
                #delta=None
            #oldTime = newTime
            try:
                image_pub.publish(bridge.cv2_to_imgmsg(frame, "bgr8"))
            except CvBridgeError as e:
                print(e)

    except KeyboardInterrupt:
        print("Exiting")
    except:
        raise
    finally:
        cap.release()
        cv2.destroyAllWindows()



if __name__ == '__main__':
    main(sys.argv)
