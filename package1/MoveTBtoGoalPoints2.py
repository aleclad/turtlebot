#!/usr/bin/env python
# MoveTBtoGoalPoints

import rospy
import actionlib       # Use the actionlib package for client and server

from move_base_msgs.msg import MoveBaseAction, MoveBaseGoal

# Define Goal Points and orientations for TurtleBot in a list
GoalPoints = [ [(0.23, -1.62, 0.0), (0.0, 0.0, 0.0, 1.0)] ,
[(-1.67, -3.43, 0.0), (0.0, 0.0, 0.0, 1.0)], [(0.23, -1.62, 0.0), (0.0, 0.0, 0.0, 1.0)] ,
[(-1.67, -3.43, 0.0), (0.0, 0.0, 0.0, 1.0)], [(0.23, -1.62, 0.0), (0.0, 0.0, 0.0, 1.0)] , 
[(-1.67, -3.43, 0.0), (0.0, 0.0, 0.0, 1.0)], [(0.23, -1.62, 0.0), (0.0, 0.0, 0.0, 1.0)] ,
[(-1.67, -3.43, 0.0), (0.0, 0.0, 0.0, 1.0)] ]


# 4 ish iterations above

# The function assign_goal initializes the goal_pose variable as a MoveBaseGoal action type.
#
print("You have 20 seconds until movement begins...")
rospy.sleep(5)  #sleep for some seconds

def assign_goal(pose):  

    goal_pose = MoveBaseGoal()        
    goal_pose.target_pose.header.frame_id = 'map'
    goal_pose.target_pose.pose.position.x = pose[0][0]
    goal_pose.target_pose.pose.position.y = pose[0][1]
    goal_pose.target_pose.pose.position.z = pose[0][2]
    goal_pose.target_pose.pose.orientation.x = pose[1][0]
    goal_pose.target_pose.pose.orientation.y = pose[1][1]
    goal_pose.target_pose.pose.orientation.z = pose[1][2]
    goal_pose.target_pose.pose.orientation.w = pose[1][3]

    return goal_pose

if __name__ == '__main__':
    rospy.init_node('MoveTBtoGoalPoints')
# Create a SimpleActionClient of a move_base action type and wait for server.
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction)  
    client.wait_for_server()
    
#       
    for TBpose in GoalPoints:  
        TBgoal = assign_goal(TBpose)   # For each goal point assign pose
        client.send_goal(TBgoal)
        success = client.wait_for_result()
#        client.wait_for_result()
    
    if success:
# if (client.get_state() == GoalStatus.SUCCEEDED):
        rospy.loginfo("success")
    else:
        rospy.loginfo("failed")





