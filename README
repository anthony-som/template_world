### 1. Install Dependencies
Run these commands to install the required simulation and control binaries.

```bash
sudo apt update
sudo apt install ros-humble-gazebo-ros2-control \
                 ros-humble-ros2-control \
                 ros-humble-ros2-controllers

```
### 2. Create a ROS 2 Workspace
Set up a ROS 2 workspace to build your custom packages.
```bash
source /opt/ros/humble/setup.bash   
mkdir -p ~/ros2_ws/src #Skip if you already have a workspace
cd ~/ros2_ws/src
git clone https://github.com/anthony-som/template_world
cd ~/ros2_ws                                                                                                                                                  
colcon build --packages-select template_world                                                                                                                 
source install/setup.bash  
```
### 3. Run the Simulation
Launch the Gazebo simulation with the provided world and robot configuration.
```bash
ros2 launch template_world gazebo_launch.py
```