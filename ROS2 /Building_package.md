## While inside ros_env and in the desired directory 
- Create a new workspace using 'rosws add **name of the worspace**' jazzy and complete it by using 'colcon build'
- Create a directory inside this workspace named src 'mkdir src' and enter src 'cd src'
- Create a specific package using 'ros2 pkg create **package name** --build-type ament_python(**or ament_cmake**) --dependencies rclpy'
- Back to the workspace directory and 'colcon build' again

- Create a file inside the folder inside the folder with the package name 'touch **node name**'
- Write the node code
- Turn this file into a useful file 'chmod +x **node file name**'
- Inside the setup.py file in the package, change entry_points, console_scripts '["**node program name** = **package_name.node_file_namepublish:main**"]'
- Activate the workspace by using 'rosws **name of the workspace**'
- After 'colcon build' again, you can call this file buy using 'ros2 run **package name** **program name**'
- In the package.xml file add the libraries used
