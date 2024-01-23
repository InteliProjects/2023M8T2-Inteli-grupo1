# Non-funtional Requirement 1
# Description: The system must be able to process texts or speech commands in less than 2 seconds
# Evaluation method: The robot will process the command and the time it takes to process it will be measured

import sys
# sys.path.append('../src/ros2_ws/src/navigation-cli-python/navigation-cli-python')
sys.path.append('../src/bridge/stt')
# from cli import create_pose_stamped, getCoordinates
from stt import STT

import unittest
from timer import Timer

class TestRobotNavigation(unittest.TestCase):
    def setUp(self):
        
        self.timer = Timer()
        self.stt_ = STT(filename='./audio/Audio2.ogg')

    def test_get_coordinates(self):

        self.timer.start()
        coordinates = getCoordinates("Quero que você vá ao ponto 1.0 2.0")
        self.assertEqual(coordinates, [1.0, 2.0])
        self.timer.stop()

    def test_speech_to_text(self):

        self.timer.start()
        speech_text = self.stt_.transcribe()
        print(speech_text)
        self.timer.stop()

if __name__ == '__main__':
    unittest.main()