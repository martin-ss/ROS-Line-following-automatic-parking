# ROS-Line-following-automatic-parking

# ROS_TurtleBot3

## Abstract

* Demonstration of tutlebot3 robot control and simulation is achieved through
  different completed tasks, which in order to be solved, a certain skills related
  to ROS basics in programming and architecture understanding should be
  mastered as , on top of that, Our simulated ROS
  environment provided by The-Construct website is exploited with the
  different provided ROS online courses as well as technical mentoring. As a
  result, our implementation been able to achieve the 4 requested tasks. In this
  report, a detailed guideline about the implementation will be presented in
  order for the reader to be able to implement it him/her self.


## See DEMO examples:

* <https://drive.google.com/drive/folders/191sR8DYO83IFeH6Y3nk76CO7pdj95PTV?usp=sharing>

## Introduction

*TurtleBot3 is a one low-cost, personal robot with open-source software, that can
  perform different interesting goals. According to [1], TurtleBot3 is a small,
  affordable, programmable, ROS-based mobile robot for use in education, research,
  hobby, and product prototyping. The goal of TurtleBot3 is to dramatically reduce
  the size of the platform and lower the price without having to sacrifice its
  functionality and quality, while at the same time offering expand-ability. The
  TurtleBot3’s core technology is SLAM, Navigation and Manipulation, making it
  suitable for home service robots. The TurtleBot can run SLAM(simultaneous
  localization and mapping) algorithms to build a map and can drive around the
  environment. Also, it can be controlled remotely from a laptop, joy-pad or
  Android-based smart phone as described in [2]. The TurtleBot can also follow a
  person’s legs as they walk in a room. Our goal is to implement 4 different robotics
  tasks on Turtlebot3 robot, that is based on mainly on knowing how to use ROS to
  manipulate the robot, simulate an environment, Path planning and localization and
  way-points following.
  
  
## Pipeline
![alt text](https://github.com/martin-ss/ROS_TurtleBot3/blob/main/Report/FINAL%20REPORT_MARTIN%20EMILE-04.png?raw=true)

## Table of contents

Use for instance <https://github.com/ekalinin/github-markdown-toc>:

> * [Title / Repository Name](#TurtleBot3)
>   * [About / Synopsis](#Abstract)
>   * [Table of contents](#table-of-contents)
>   * [Installation](#installation)
>   * [Usage](#usage)
>     * [Screenshot of the Environment](#screenshot-of-the-Environment)
>     * [Task 1 Steps](#features)
>     * [Task 2 Steps](#features)
>     * [Task 3 Steps](#features)
>     * [Task 4 Steps](#features)
>   * [Refrencess](#Refrencess)


>   * [About the Project](#)


## Installation

Sample:

* From the Crrent repo: git clone  https://github.com/martin-ss/ROS_TurtleBot3


## Usage

* This project is aimed to control the navigation of TurtleBot3 in a given environment through Mapping, Localization and Path Planning

### Screenshot of the Environment

![alt text](https://github.com/martin-ss/ROS_TurtleBot3/blob/main/ros2.png?raw=true)

## Task 1

1-Open a Linux shell window\
2- Enter “ $ rostopic list -grep /cmd_vel” to make sure the topic exist\
3-Enter “$ rosmsg show geometry_msgs / Twist” to see the structure of the messge\
you want to send through the topic\
4- Finally, Enter “$rostopic pub / cmd_vel geometry_msgs / Twist - '[2.0, 0.0, 0.0]'
'[0.0, 0.0, 0.0]'” to see the robot moving in the x direction.\


## Task 2

1- Extract my implemented package that comes along with this report\
2- Place it in your Catkin_ws/src file\
3- Before we start launching launch files, I would recommend to take a look at [4]
for some information about the g_mapping node\
4- Launch Rviz to visualize the mapping process\
5- Launch the “start_mapping.launch” launch file\
6- Move the robot using the keyboard launch file\
7- Visualize the mapping while being built\
8- Make a directory to place the map files\
9- Save the Map\
10- For the localization part, launch “start_localization.launch” file\
11- Add a PoseArray into your Rviz that subscribe to /ParticleCloud12- Move the robot using the Keyboard\
12- Observe the red arrows getting denser on the location of the robot\


## Task 3

1- Extract my implemented package that comes along with this report\
2- Place it in your Catkin_ws/src file\
3- For the path planning and navigation, launch the “ start_navigation.launch”
launch file\
4- Launch Rviz to visualize the navigation process\
5- Using Rviz 2D naviagte button, send a position in the environment\
6- Kindly, note, the obstcale avoidance is already taken into account because we
already mapped the environment with all the existing obstacles\
7- Visualize the navigation process\
8- Observe the path taken by the robot\


## Task 4

First method, choosing way points manually\
1- Extract my implemented package that comes along with this report\
2- Place it in your Catkin_ws/src file\
3- Clone this library https://github.com/danielsnider/follow_waypoints4- Launch the “ start_navigation.launch” launch file that in the t3_navigation
package\
4- Launch the “follow_waypoint.launch” launch file that is in the cloned package\
5- Start Rviz for visualizing\
6- Add A PoseArray to your Rviz that subscribe to the topic /way_points\
7- Choose your way points using the Rviz 2D Pose Est. button\
8- After choosing your way points, publish into the topic /path_ready\
9- Observe the robot follow the specified way points\\\

Second method, choosing way points using a python script\
1- Extract my implemented package that comes along with this report\
2- Place it in your Catkin_ws/src file\
3-Launch the “ start_navigation.launch” launch file that in the t3_navigation
package\
4- Launch the “start_follow_waypoint.launch” launch file that is included in my
package\
5- Start Rviz for visualizing or Gazebo\
6- Add A PoseArray to your Rviz that subscribe to the topic /way_points\
7- Specifiy your way_points in the python file titled “waypoint_publisher.py”\
8- After choosing your way points, publish into the topic /path_ready using the
python file “waypoint_publisher.py” so just execute this file\
9- Observe the robot follow the specified way points\


## Process (Steps)
![alt text](https://github.com/martin-ss/ROS_TurtleBot3/blob/main/Report/FINAL%20REPORT_MARTIN%20EMILE-09.png?raw=true)
![alt text](https://github.com/martin-ss/ROS_TurtleBot3/blob/main/Report/FINAL%20REPORT_MARTIN%20EMILE-10.png?raw=true)
![alt text](https://github.com/martin-ss/ROS_TurtleBot3/blob/main/Report/FINAL%20REPORT_MARTIN%20EMILE-11.png?raw=true)
![alt text](https://github.com/martin-ss/ROS_TurtleBot3/blob/main/Report/FINAL%20REPORT_MARTIN%20EMILE-12.png?raw=true)


## Refrencess

[1] https://emanual.robotis.com/docs/en/platform/turtlebot3/overview/ \
[2] https://www.roscomponents.com/en/mobile-robots/214-turtlebot-3.html#/courses-no \
[3] Book "ROS Robotics Projects" \
[4] http://wiki.ros.org/gmapping \
[5] Course titled “Mastering with ROS: Turtlebot3” \
[6] Course titled “ROS Navigation in 5 days” \
[7] http://wiki.ros.org/ROS/Tutorials/ExaminingPublisherSubscriber \
[8] http://wiki.ros.org/navigation 

## About The TurtleBot3 Project
It is impelemneted as a part of a course module named Robotics Project for Master-2 
