#!/usr/bin/env python
import roslib; roslib.load_manifest('aribo')
import rospy

import hokuyo_node
import sensor_msgs.msg

def callback(data):
    print data.ranges[540]
    pass

def laser_listener():
    pass
    rospy.init_node('laser_listener', anonymous=True)
    rospy.Subscriber("/scan",sensor_msgs.msg.LaserScan,callback)
    rospy.spin()

if __name__ == '__main__':
    laser_listener()