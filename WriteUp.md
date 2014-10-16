A* Team Write Up
=======================
Elizabeth Duncan, Jack Fan, and Marena Richardson


The goal of our project was to better understand path planning by implementing A* with the Neato robot. 

We solved this problem by mapping a closed environment (the Star center) using SLAM, importing and processing that image using numpy, and creating our own A* framework. The A* framework was based on our own Node class for every location (from an occupancy grid of every pixel). It also involved designing our own heuristic which was created by assigning costs to every robot move. 

The code was structured into four main files. Mapcut.py cropped the huge image created from ROS built-in SLAM and just focused on the part of the map that had objects or open space. Map_manipulation.py read in the cropped environment image and added a buffer to all objects. This buffer was approximately the width of the Neato itself. Astar.py read in the environment map (with any additional buffers from map_manipulation.py) and returned a path of pixels. This is the “best” path created from our A* heuristic. Finally, followpixels.py converted the pixel path to meter points (where the starting position of the neato is 0,0 meters). It then read in odometry data and drove the Neato using proportional control based on its position and the meter path.

A major design decision for our team was how to get the Neato to follow the returned path from astar.py. We decided to use odometry because it seemed like a quick and easy implementation - since there is an odometry topic published by the Neato. Unfortunately, this system ended up being one of the most difficult and - of the whole system - has the most to improve. The odometry system currently accumulates error. Future work could possibly incorporating laser scans to decrease this would be ideal. Alternatively, a particle filter could be used to better localize the robot and fix error. 

Lessons for future robotics projects is to not leave the physical system for last. This is probably the part that needs the most work and will be the most difficult. Push this work to the front so that the most time can be spent where it is needed!

