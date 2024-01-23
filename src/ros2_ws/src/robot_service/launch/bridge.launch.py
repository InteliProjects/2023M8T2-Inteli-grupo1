
import os
from launch import LaunchDescription,LaunchService
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch.launch_description_sources import PythonLaunchDescriptionSource
import subprocess


def generate_launch_description():

    map = input("Enter the map name: ")

    saved_map = IncludeLaunchDescription(PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('turtlebot3_navigation2'), 'launch'), '/navigation2.launch.py']), launch_arguments={'use_sim_time': 'False', 'map':f'../maps/{map}.yaml'}.items())


    turtlesim_world_1 = IncludeLaunchDescription(
    PythonLaunchDescriptionSource([os.path.join(
        get_package_share_directory('turtlebot3_gazebo'), 'launch'),
        '/turtlebot3_world.launch.py'])

    )



#saved_map,
    return LaunchDescription([
        saved_map,
        turtlesim_world_1,



    ])


if __name__ == '__main__':
    ls = LaunchService()
    ls.include_launch_description(generate_launch_description())
    ls.run()
