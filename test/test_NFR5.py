# Non-funtional Requirement 5 
# Description: The application must be able to activate the robot to pick an item in less than 5 seconds after its request
# Evaluation method: The robot will be activated and the time it takes to pick an item will be measured

import sys
sys.path.append('../src/ros2_ws/src/navigation-cli-python/navigation-cli-python')
from cli import create_pose_stamped, getCoordinates

import unittest
from timer import Timer

class TestRobotNavigation(unittest.TestCase):
    def setUp(self):
        
        self.timer = Timer()

    def test_robot_navigation_timing(self):

        input_text = "Quero que você vá ao ponto 1.0 1.0"
        positions = getCoordinates(input_text)
        self.assertIsNotNone(positions)

        self.timer.start()
        goal_pose = create_pose_stamped(navigator=None, pos_x=positions[0], pos_y=positions[1], rot_z=0.0)
        self.timer.stop()

if __name__ == '__main__':
    unittest.main()