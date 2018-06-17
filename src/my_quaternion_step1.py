#!/usr/bin/env python
import rospy
import math
from sensor_msgs.msg import Imu
from tf.transformations import euler_from_quaternion, quaternion_from_euler

roll = pitch = yaw = 0.0

def get_rotation (msg):
    global roll, pitch, yaw
    orientation_q = msg.orientation
    #print msg.orientation
    orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
    (roll, pitch, yaw) = euler_from_quaternion (orientation_list)
    #rospy.sleep(1) # Sleeps for 1 sec 
    #print yaw

rospy.init_node('my_quaternion_to_euler')
sub = rospy.Subscriber ('/imu', Imu, get_rotation)
r = rospy.Rate(0.0017)  # about every 10 minutes (=1/(60 seconds X 10 min))
while not rospy.is_shutdown():  
    #quat = quaternion_from_euler (roll, pitch,yaw)
    #print quat
    #rospy.sleep(1) # Sleeps for 1 sec
    print math.degrees(yaw)
    # degrees = (degrees + 360) % 360;  // +360 for implementations where mod returns negative numbers
    degrees360 = (math.degrees(yaw) + 360) % 360
    print degrees360
    r.sleep()