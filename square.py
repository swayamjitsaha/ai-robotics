#!/usr/bin/env python3
import rospy
import numpy
from geometry_msgs.msg import Twist

rospy.init_node('square', anonymous=True)
pub = rospy.Publisher('turtle1/cmd_vel', Twist, queue_size=10)
rate = rospy.Rate(1) # 10hz
PI = 3.1415926535897

print('Starting square . . .')

# TODO: Modify the code below so that the robot moves in a square

#while not rospy.is_shutdown():
    
for i in range(6):
    twist = Twist()

    twist.linear.x = 0.5
    twist.angular.z = 0
    pub.publish(twist)
    rate.sleep()
    
for i in range(1):
    twist = Twist()

    twist.linear.x = 0
    twist.angular.z = PI/2
    pub.publish(twist)
    rate.sleep()
    
for i in range(6):
    twist = Twist()

    twist.linear.x = 0.5
    twist.angular.z = 0
    pub.publish(twist)
    rate.sleep()
    
for i in range(1):
    twist = Twist()

    twist.linear.x = 0
    twist.angular.z = PI/2
    pub.publish(twist)
    rate.sleep()
    
for i in range(6):
    twist = Twist()

    twist.linear.x = 0.5
    twist.angular.z = 0
    pub.publish(twist)
    rate.sleep()
    
for i in range(1):
    twist = Twist()

    twist.linear.x = 0
    twist.angular.z = PI/2
    pub.publish(twist)
    rate.sleep()
    
for i in range(6):
    twist = Twist()

    twist.linear.x = 0.5
    twist.angular.z = 0
    pub.publish(twist)
    rate.sleep()
    
for i in range(1):
    twist = Twist()

    twist.linear.x = 0
    twist.angular.z = PI/2
    pub.publish(twist)
    rate.sleep()

#while not rospy.is_shutdown():
 #   twist = Twist()

 #   twist.linear.x = 0.5
 #   twist.angular.z = PI/2
 #   pub.publish(twist)
 #   rate.sleep()
        
#pub.publish(twist)
#rate.sleep() #sleep until the next time to publish
