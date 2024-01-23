
import os
from launch import LaunchDescription,LaunchService
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    
    map = input("Enter the map name: ")
    simulation = input("Enter 1 for simulation or 0 for real robot: ")
    saved_map = IncludeLaunchDescription(PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('turtlebot3_navigation2'), 'launch'), '/navigation2.launch.py']), launch_arguments={'use_sim_time': 'False', 'map':f'../maps/{map}.yaml'}.items())


    robot_controler = Node(
            package='jose_entregas',
            executable='llm_robot',

        )
    #uncoment if not using real robot
    turtlesim_world_1 = IncludeLaunchDescription(
    PythonLaunchDescriptionSource([os.path.join(
        get_package_share_directory('turtlebot3_gazebo'), 'launch'),
        '/turtlebot3_world.launch.py'])
        
    )
    if simulation == '1':
        return LaunchDescription([
        
        saved_map,
        turtlesim_world_1,
        robot_controler
    ])
    else:

        return LaunchDescription([
            
            saved_map,
            robot_controler
        ])

#ros2 launch nav2_bringup bringup_launch.py use_sim_time:=False autostart:=False map:=path/to/map.yaml
if __name__ == '__main__':
    ls = LaunchService()
    ls.include_launch_description(generate_launch_description())
    ls.run()