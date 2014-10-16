A* Team Write Up
=======================
Elizabeth Duncan, Jack Fan, and Marena Richardson


The goal of our project was to better understand path planning by implementing A* with the Neato robot. 

We solved this problem by mapping a closed environment (the Star center) using SLAM, importing and processing that image using numpy, and creating our own A* framework. The A* framework was based on our own Node class for every location (from an occupancy grid of every pixel). It also involved designing our own heuristic which was created by assigning costs to every robot move. 

The code was structured into four main files. Mapcut.py cropped the huge image created from ROS built-in SLAM and just focused on the part of the map that had objects or open space. Map_manipulation.py read in the cropped environment image and added a buffer to all objects. This buffer was approximately the width of the Neato itself. Astar.py read in the environment map (with any additional buffers from map_manipulation.py) and returned a path of pixels. This is the “best” path created from our A* heuristic. Finally, followpixels.py converted the pixel path to meter points (where the starting position of the neato is 0,0 meters). It then read in odometry data and drove the Neato using proportional control based on its position and the meter path.

A major design decision for our team was how to get the Neato to follow the returned path from astar.py. We decided to use odometry because it seemed like a quick and easy implementation, since there is an odometry topic published by the Neato. Unfortunately, this system ended up being one of the most difficult pieces to implement. The odometry system initially was accumulating error in how far it thought it was from the waypoints it chose in the list of coordinates. Each time it thought it was farther away. After struggling with this for days, we ran the code in gazebo to be sure the problem was with our code not the robot, and we found a bug. The vectors to the waypoints were being calculated from the origin each time, and not from the previous waypoint. Fixing this bug fixed the problem and the robot got within 0.1 meters of all the waypoints. 

Once this piece had been fixed, running the code revealed that the path that astar had planned did not seem to be perfectly aligned with the actual layout of the star center. The robot appeared to be making the correct turns and thought it was following the path, but it was still running into obstacles and not quite reaching the goal. We tried many approaches to fix it, including biasing the pixels to be slightly rectangular to try and adjust for the fact that the robot did not seem to be moving enough laterally and changing the robot’s initial orientation, but we had no success. This remains the primary unsolved question of our project; Why does the path not align correctly with the real star center? Future work on this project would involve trying to correct this problem. If the problem has to do with accumulated error in the odometry frame, a particle filter could be used to better localize the robot and help the odometry frame adjust as the robot navigates.

The main lesson we learned for future robotics projects is not to leave the physical system for last. This is probably the part that needs the most work and will be the most difficult. Push this work to the front so that the most time can be spent where it is needed!