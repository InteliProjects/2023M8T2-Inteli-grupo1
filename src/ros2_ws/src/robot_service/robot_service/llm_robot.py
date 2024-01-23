#! /usr/bin/env python3
import rclpy
from rclpy.node import Node
from nav2_simple_commander.robot_navigator import BasicNavigator
from .auxliar_functions import move_to,generate_initial_pose,sort_points, get_input_position
from std_msgs.msg import String
from collections import deque
import re
from robot_service.llm import LLM_model


class ChatBotModel(Node):
    def __init__(self, nav):
        super().__init__('llm_node')
        self.nav = nav
        self._publisher = self.create_publisher(String, 'whatsApp_topic', 10)
        self._subscriber = self.create_subscription(
        String,
        'llm_topic',
        self.listener_callback,
        10)
        self.queue = deque()
        self._logger = self.get_logger()
        self.get_logger().info("Iniciei")
        self._msg = String()
        self._model = LLM_model()

    def listener_callback(self, msg):
        """
        This function purpose is to processes data from the llm_topic
        """
        self._logger.info(f'Robot received: {msg.data}')
        if str(msg.data).lower() == "run":
            self._logger.info(f'/run -> Iniciei a rota: {self._msg.data}')
            if self.nav.isTaskComplete() and self.queue:
                self._logger.warning(f'Passing data to navigation controller  {self.queue}')
                self.queue=sort_points(self.queue,self)
                self._logger.info(f'Andando...')
                move_to(self,self.nav)  

                
        else:
            output_text = self._model.chat(msg.data)
            self.get_logger().info('Model output: ' + output_text)
            feedback_msg = String()
            feedback_msg.data = f'-> {output_text}'
            self._publisher.publish(feedback_msg)
            position = get_input_position(self,output_text)
            if position:
                self._logger.info(f'Adicionei a posição: {position}')
                self.queue.append(position)
                

def main():
    
    
    rclpy.init()
    nav = BasicNavigator()
    generate_initial_pose(nav)
    node = ChatBotModel(nav)
    rclpy.spin(node)
    node.destroy_node()
    rclpy.shutdown()
if __name__ == "__main__":
    main()
