#!/usr/bin/env python
# license removed for brevity
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import Bool

# This script will listen for joystick button 5 being toggled and
# send zero speed messages to the mux to disable the follower until
# button 5 is pressed again.

class BehaviorSwitch(object):
    def __init__(self):
        self.running = False

    def callback(self, bool_msg):
        if bool_msg.data == False: 
            self.running = False
	    print("stop follower")
	else: 
	    print("start follower")
	    self.running = True
        rospy.loginfo(repr(bool_msg))

    def run(self):
        rospy.init_node('behavior_switch', anonymous=True)
        pub = rospy.Publisher('cmd_vel_mux/input/switch', Twist, queue_size=10)
        rospy.Subscriber('chatter', Bool, self.callback)
        rate = rospy.Rate(10)
        while not rospy.is_shutdown():
            if self.running:
                empty_msg = Twist()
                pub.publish(empty_msg)
            rate.sleep()

if __name__ == '__main__':
    try:
        behavior_switch = BehaviorSwitch()
        behavior_switch.run()
    except rospy.ROSInterruptException:
        pass
#####################
 

