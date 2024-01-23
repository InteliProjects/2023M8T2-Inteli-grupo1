#! /usr/bin/env python3
import rclpy
from nav2_simple_commander.robot_navigator import BasicNavigator
from .auxliar_functions import move_to,generate_initial_pose,sort_points
from rclpy.node import Node
from std_msgs.msg import String


class Robot(Node):
    def __init__(self,nav):
        super().__init__('robot_node')
        self.nav = nav
        self.queue = []
        self.extra_queue = []
        self._subscriber = self.create_subscription(
            String,
            'chatbot_topic',
            self.listener_callback,
            10)
        self._logger = self.get_logger()
        self.feedback= self.create_publisher(String, 'feedback_topic', 10)

      
      

    def listener_callback(self, msg):
        """ 
        This function purpose is to receive the data from the chatbot topic and pass it to the navigation controller
        """
        self._logger.info(f'Robot received: {msg.data}')
       
        self._logger.warning('Passing data to navigation controller')
        if msg.data == "run":
            self.queue.extend(self.extra_queue)
            self.extra_queue.clear()
            self.queue=sort_points(self.queue)
            move_to(self,self.nav)  

            

                
        else:
            if self.nav.isTaskComplete():
                self.queue.append([float(s) for s in msg.data.split(',')])
            else :
                self.extra_queue.append([float(s) for s in msg.data.split(',')])

        



def main():
    rclpy.init()

    nav = BasicNavigator()
    
    
    robot = Robot(nav)

    generate_initial_pose(nav)

    rclpy.spin(robot)
    

if __name__ == '__main__':
    main()
