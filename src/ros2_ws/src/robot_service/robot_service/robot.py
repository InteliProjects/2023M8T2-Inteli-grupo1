#! /usr/bin/env python3

import re
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
from nav2_simple_commander.robot_navigator import TaskResult

from .navigation_controller import Navigation

class Robot(Node):
    def __init__(self):
        super().__init__('robot_node')
        self._publisher = self.create_publisher(String, 'whatsApp_topic', 10)
        self._subscriber = self.create_subscription(
            String,
            'chatbot_topic',
            self.listener_callback,
            10)
        self._logger = self.get_logger()
        self._msg = String()
        self._nav = Navigation()

    def listener_callback(self, msg):
        """
        This function purpose is to receive the data from the chatbot topic
        """
        self._logger.info(f'Robot received: {msg.data}')
        self._logger.warning('Passing data to navigation controller')
        self._msg = msg.data
        return self._msg


    def get_input_position(self):
        """
        This function purpose is to get the position from the chatbot
        using a regex, then returning it as a list of integers
        """
        input_text = self.listener_callback()
        match = re.findall(r'[-+]?(\d*\.\d+|\d+)([eE][-+]?\d+)?', input_text)
        position = [int(match) for i in match[-2:]]
        return position

    def move_towards_required_position(self):
        """
        This function purpose is to create a pose and move the robot
        """
        position = self.get_input_position()
        self._nav.create_pose(position[0], position[1], 0.0)

    def cheking_status(self):
        """
        Checks the status of a task after moving towards the required position.
        Returns:
        bool: True if the task is completed successfully, False otherwise.
        """
        self.move_towards_required_position()
        task_status = self._nav.robot_navigation_status()

        return task_status if task_status == TaskResult.SUCCEEDED else False

def main():
    rclpy.init()
    robot = Robot()
    rclpy.spin(robot)
    robot.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
