import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    pkg_path = get_package_share_directory('template_world')
    world_file_path = os.path.join(pkg_path, 'worlds', 'template.world')
    models_path = os.path.join(pkg_path, 'models')

    gazebo_ros_path = get_package_share_directory('gazebo_ros')

    # Append our models directory to GAZEBO_MODEL_PATH
    existing = os.environ.get('GAZEBO_MODEL_PATH', '')
    model_path = models_path + ':' + existing if existing else models_path

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(gazebo_ros_path, 'launch', 'gazebo.launch.py')
        ),
        launch_arguments={'world': world_file_path}.items()
    )

    return LaunchDescription([
        SetEnvironmentVariable('GAZEBO_MODEL_PATH', model_path),
        gazebo
    ])
