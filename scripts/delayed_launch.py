#!/usr/bin/env python

import rospy
import roslaunch
import time
import sys

def main():
    print("Start")
    rospy.init_node('delayed_launch', anonymous=True)
    
    uuid = roslaunch.rlutil.get_or_generate_uuid(None, False)
    roslaunch.configure_logging(uuid)

    launch_file = rospy.get_param('~launch_file')
    delay_zed = rospy.get_param('~delay')
    delay_server_vr = rospy.get_param('~delay')
    delay_vive = rospy.get_param('~delay')
    delay_vive_tracker_tiago = rospy.get_param('~delay')

    launch_args = None

    #_launch_args = rospy.get_param('~launch_args').split("; ")
    # print(_launch_args)

    time.sleep(delay_zed)
    time.sleep(delay_server_vr)
    time.sleep(delay_vive)
    time.sleep(delay_vive_tracker_tiago)

    if launch_args is not None:
        launch = roslaunch.parent.ROSLaunchParent(uuid, [(launch_file, launch_args)])
    else:
        launch = roslaunch.parent.ROSLaunchParent(uuid, [launch_file])
    
    launch.start()
    
    rospy.spin()

if __name__ == '__main__':
    main()

