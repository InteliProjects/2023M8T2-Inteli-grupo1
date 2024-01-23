FROM tiryoh/ros2-desktop-vnc:humble

# Ros2, Gazebo, Nav2, and Turtlebot3 environment

## Arguments
ARG ROS_DISTRO=humble
ARG TURTLEBOT3_MODEL=burger
ARG PROJECT_FOLDER=project_ws

## Set environment variables
ENV GAZEBO_MODEL_PATH="/opt/ros/${ROS_DISTRO}/share/turtlebot3_gazebo/models:${GAZEBO_MODEL_PATH}"
ENV TURTLEBOT3_MODEL=${TURTLEBOT3_MODEL}
ENV ROS_DOMAIN_ID=30
ENV ROS_DISTRO=${ROS_DISTRO}
ENV ROS_LOCALHOST_ONLY=0
ENV ROS_PYTHON_VERSION=3
ENV ROS_VERSION=2
ENV RMW_IMPLEMENTATION=rmw_cyclonedds_cpp

## Update and upgrade packages
RUN sudo apt install ros-${ROS_DISTRO}-navigation2 ros-${ROS_DISTRO}-nav2-bringup ros-${ROS_DISTRO}-turtlebot3* ros-${ROS_DISTRO}-rmw-cyclonedds-cpp \
	ros-${ROS_DISTRO}-nav2-simple-commander ros-${ROS_DISTRO}-tf-transformations python3-transforms3d \
	-y && \
	sudo apt-get clean && \
	sudo rm -rf /var/lib/apt/lists/

# Project workspace

## Setup ubuntu workspace from local workspace
COPY ./${PROJECT_FOLDER} /home/ubuntu/${PROJECT_FOLDER}

## Build project
RUN . /opt/ros/${ROS_DISTRO}/setup.bash

## Modify burger.yaml to use differential motion model
RUN if [ -f /opt/ros/${ROS_DISTRO}/share/turtlebot3_navigation2/param/burger.yaml ]; then \
	sed -i 's/robot_model_type: "differential"/robot_model_type: "nav2_amcl::DifferentialMotionModel"/' /opt/ros/${ROS_DISTRO}/share/turtlebot3_navigation2/param/burger.yaml; \
	fi