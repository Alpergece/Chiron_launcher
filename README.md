# Chiron_launcher
Chiron_launcher is a ROS package designed to facilitate teleoperation. It does this by launching both the vision and control pipelines. By providing an organized way to initiate these systems, the package ensures seamless teleoperation.

To launch these pipelines, you can use the following commands:

Launching the Vision Pipeline:
The vision pipeline starts the ZED Camera, Vive VR System, Vive VR Tracker together with a reasonable delay between. 
Run the following command in your terminal:

$ roslaunch chiron_launcher vision_pipeline.launch

Launching the Control Pipeline:
The control pipeline takes the processed data from the vision pipeline and translates it into control commands that can be executed by the robot. It starts Kalman Filter + null space control, head control, right arm control, left arm control, gripper control  
Use the following command to start the control pipeline:

$ roslaunch chiron_launcher control_pipeline.launch

Remember, before running these commands, source your ROS workspace. Also ensure that your workspace's 'setup.bash' file is sourced in every new terminal where you intend to interact with your ROS system.

Feel free to contribute to or report issues with this package. 