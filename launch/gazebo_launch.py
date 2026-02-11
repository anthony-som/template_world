import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    # 1. Get the path to your package and world file
    pkg_path = get_package_share_directory('template_world') # Double check this name!
    world_file_path = os.path.join(pkg_path, 'worlds', 'template.world')

    # 2. Get the gazebo_ros package path for the empty_world launch
    gazebo_ros_path = get_package_share_directory('gazebo_ros')

    # 3. Create the Gazebo launch action
    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(gazebo_ros_path, 'launch', 'gazebo.launch.py')
        ),
        launch_arguments={'world': world_file_path}.items()
    )

    # 4. RETURN the LaunchDescription (Crucial step!)
    return LaunchDescription([
        gazebo
    ])