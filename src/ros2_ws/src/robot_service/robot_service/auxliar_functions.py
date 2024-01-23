from transformations import quaternion_from_euler
from geometry_msgs.msg import PoseStamped
import re
from python_tsp.exact import solve_tsp_dynamic_programming
import math
import numpy as np
from collections import deque



def get_input_position(self,text):
    """
    This function purpose is to get the position from the chatbot
    using a regex, then returning it as a list of float
    """
    input_text = text
    self._logger.info(f'Robot received: {text}')
    match = re.findall(r'[-+]?(\d*\.\d+|\d+)([eE][-+]?\d+)?', input_text)
    position = [float(i[0]) for i in match]
    self._logger.info(f'position: {position}')
    if len(position) > 1:
        return [position[0],position[1]]
    self._logger.info(f'Erro ao detectar as peças: { len(position) }')

    return


def create_pose_stamped( pos_x, pos_y, rot_z,nav) -> PoseStamped:
    """Creates a position in the map frame with the given coordinates and rotation"""
    q_x, q_y, q_z, q_w = quaternion_from_euler(0.0, 0.0, rot_z)
    pose = PoseStamped()
    pose.header.frame_id = 'map'
    pose.header.stamp = nav.get_clock().now().to_msg()
    pose.pose.position.x = pos_x
    pose.pose.position.y = pos_y
    pose.pose.position.z = pos_x
    pose.pose.orientation.x = q_x
    pose.pose.orientation.y = q_y
    pose.pose.orientation.z = q_z
    pose.pose.orientation.w = q_w
    return pose


def generate_initial_pose(nav)-> None:
    """sets the initial pose of the robot to the origin so that nav2 can start"""
    q_x, q_y, q_z, q_w = quaternion_from_euler(0.0, 0.0, 0.0)
    initial_pose = PoseStamped()
    initial_pose.header.frame_id = 'map'
    initial_pose.header.stamp = nav.get_clock().now().to_msg()
    initial_pose.pose.position.x = 0.0
    initial_pose.pose.position.y = 0.0
    initial_pose.pose.position.z = 0.0
    initial_pose.pose.orientation.x = q_x
    initial_pose.pose.orientation.y = q_y
    initial_pose.pose.orientation.z = q_z
    initial_pose.pose.orientation.w = q_w


    nav.setInitialPose(initial_pose)
    nav.waitUntilNav2Active()


def move_to(self,nav)-> None:
    waypoints = []
    """moves the robot next the  position in the queue"""
    if len(self.queue) == 0:
        return
    while len(self.queue) > 0:
        positions = self.queue.pop()
        position = create_pose_stamped(positions[0],positions[1],0.0,nav)
        waypoints.append(position)
        nav.get_logger().info('reached  point ' + str(position))

    nav.followWaypoints(waypoints)




def sort_points(points, self)-> deque:


    _points = points.copy()


    _points.appendleft([0.0,0.0])
    self._logger.info(f'Pontos apos apennd: {_points}')

    """sorts the points in the list of points using the travelling salesman problem algorithm"""
    distance_array = []
    distance_for_point = []
    for point1 in _points:
        for point2 in _points:
            #self._logger.info(f'Pontos no for: 1:{point1}, 2:{point2}')
            distance_for_point.append(math.dist(point1,point2))
        distance_array.append(distance_for_point)
        distance_for_point = []


    permutation, _ = solve_tsp_dynamic_programming(np.array(distance_array))


    sorted_points = deque()
    for i in permutation:
        sorted_points.append(_points[permutation[i]])


    sorted_points.append(sorted_points.popleft())
    self._logger.info(f'Pontos: {sorted_points}')
    return sorted_points
