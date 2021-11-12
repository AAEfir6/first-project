
<p align="center">

  <h3 align="center">PolyU ENG1003 AAE Freshman Project Group 6</h3>

</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary><h2 style="display: inline-block">Table of Contents</h2></summary>
  <ol>
    <li>
      <a href="#Background-of-Path-Planning-to-Aviation-Engineering">Background of Path Planning to Aviation Engineering</a>
    </li> 
    <li>
      <a href="#Theory-of-Path-Planning-Algorithm">Theory of Path Planning Algorithm</a>
    </li>
    <li>
      <a href="#Introduction-of-the-Engineering-Tools">Introduction of the Engineering Tools</a>
    </li>
    <li>
      <a href="#Task1">Task 1: Methodology, Results and Discussion</a>
    </li>
    <li>
      <a href="#Task2-1">Task 2.1: Methodology, Results and Discussion</a>
    </li>
    <li>
      <a href="#Task2-2">Task 2.2: Methodology, Results and Discussion</a>
    </li>
    <li>
      <a href="#Task3">Task 3: Methodology, Results and Discussion</a>
    </li>
    <li>
      <a href="#Task4-1-Adding-Checkpoints">Additional Task 4.1 Adding Checkpoints</a>
    </li>
    <li>
      <a href="#Task4-2-Changing-Environment">Additional Task 4.2 Changing Environment</a>
    </li>
    <li>
      <a href="#Task4-3-Comparing-Algorithms">Additional Task 4.3 Comparing Algorithms</a>
    </li>
    <li>
      <a href="#Reflective-Essay">Reflective Essay</a>
    </li>
    <li>
      <a href="#References">References</a>
    </li>
    
    
  </ol>
</details>


## Background of Path Planning to Aviation Engineering
<weq we qwesdfghruelgerthleriluhgrehignzi;ghe>

## Theory of Path Planning Algorithm


## Introduction of the Engineering Tools


## Acknowledgements
We use [Best-README-Template](https://github.com/othneildrew/Best-README-Template) for readme organization and [PythonRobotics](https://github.com/AtsushiSakai/PythonRobotics) for demo A star path planning.

## Task1
https://github.com/AAEfir6/first-project/blob/main/Addition%20Calculation.py<br>
a. Methodology<br>
The objective of this task is to find the flight route with the minimum achievable cost which can let the plane fly to the final destination. There is a map, the python algorithm for pathfinding, and the parameters of the aircraft to the group to calculate and obtain the objective.<br><br>
To finish task 1, the group should modified the code to match the map was given to each group. Then test the aeroplane with different parameters in the source code to find the minimum achievable cost from those 4 aeroplanes were given.<br><br>
Our group specified map was constructed in lines 288-316 in the code. The variables of the grid, starting point, ending point, obstacles, time-consuming regions, and fuel -consuming regions are stick to the map we get as the figure.
About the aircraft parameters, which is in line 50-60 in the program. We changed the corresponding perimeter to finish the task 1.<br><br>
There are in total of 4 aircraft with different parameters was given, for us to evaluate the low-cost flight plan. The parameters are CF, ΔF, CT, ΔT, C, ΔF, ΔT.


![螢幕擷取畫面 2021-10-22 112618](https://user-images.githubusercontent.com/85985312/138388655-76fe86d4-d02c-4459-b05e-30cd6e492fbc.png)

<br><br>b. Results
<br><br>PolyU-A380
<br>Cost obtained: 3297.09
<br>![A380 route](https://user-images.githubusercontent.com/85985312/140323045-407b2240-99e6-40d7-899c-8db67fc6b7a4.png)
![A380 cost](https://user-images.githubusercontent.com/85985312/140323042-f1be15ae-2744-48f2-9efc-1fd59d279229.png)
<br><br>PolyU-A381
<br>Cost obtained: 4163.58
<br>![A381 route](https://user-images.githubusercontent.com/85985312/140323049-4fe58687-85c4-47ff-be0d-994534280b88.png)
![A381 cost](https://user-images.githubusercontent.com/85985312/140323047-26d5e111-811e-43d0-b956-92f4c0c0a794.png)
<br><br>PolyU-A382
<br>Cost obtained: 5028.57
<br>![A382 route](https://user-images.githubusercontent.com/85985312/140323030-6b405f17-9d38-44eb-bddc-049a92b50e2b.png)
![A382 cost](https://user-images.githubusercontent.com/85985312/140323025-28941387-e40a-4e6e-abc4-96648ed32c1b.png)
<br><br>PolyU-A383
<br>Cost obtained: 5886.06
<br>![A383 route](https://user-images.githubusercontent.com/85985312/140323036-5aa1caf6-5cf3-4bed-9915-33600c2fb7bd.png)
![A383 cost](https://user-images.githubusercontent.com/85985312/140323033-2abcf5c4-7b2e-4df2-bc3b-5cdcd5e0ac61.png)

<br>c. Discussion
<br>In this task, the aim is to find which is the aircraft provided has the lowest cost to fight the route. In the beginning, we find that it is not easy to setup the map for the group to stimulate the flight plan. After building the map, we change the aircraft parameters to stimulate the flight. After we finish all 4 aircraft simulation, we found that the cost of aircraft PolyU-A380 is the lowest. It only cost around 3300units. Lower than others cost about 27-78%. To round up, the main focus of this task is implementing the map and knowing the algorithm. And this task allows us knowing the framework of this project we going to do.

## Task2-1
<br>a. Methodology

Linear programming—We treat C(T)=x and C(F)=y.Then We got four inequalities and drew them all in the same x-y coordinate(see the black lines),after that we could find there is a common area which is surrounded by the four lines(see the red area).On the other hand because C=x*delta_F+y*delta_T+C_c. Delta_F=delta_T=5 and C_c=a constant.Therefore C=5(x+y)+C_c.We let C(min)=Z.Then simplify it we got y>=0.2(Z-C_c)-x.It means a clust of parallel lines and we drew some of them in the former coordinate(see the blue lines).The minimum C where it is must be at the border of the red area and we found that when x=20 and y=20 comes the minimum C.
![image](https://user-images.githubusercontent.com/91596396/138546153-c3914fcb-3af8-422e-ac05-2f794d9e91fc.png)

b. Results

![image](https://user-images.githubusercontent.com/91596396/138546170-5d486cf2-d013-464e-8c5e-f96f7ed66c34.png)



![image](https://user-images.githubusercontent.com/91596396/138546174-ea40ec34-d80b-4d34-8d4f-5a5526accc11.png)

c. Discussion

This method（Linear Programming）only can be applied in Linear equation in 2 unknowns.So it is not a universal method to solve many problems.However,it is a easy way to solve Task 2-1 with just a pen and a piece of paper.We got to know from the website that there is a more convenient way to deal with the problem by using computer coding.Maybe we will try it next time.
![image](https://user-images.githubusercontent.com/91596396/138546191-5946d538-7718-43bf-96d6-3bd5e631c92c.png)


## Task2-2
a. Methodology

There are six variables, and four constraints need to be considered.

<img width="314" alt="截屏2021-10-26 12 38 24" src="https://user-images.githubusercontent.com/90883941/138809863-4e6a2741-a2f5-48f4-b164-d97d4c51d041.png">


When a parameter is changed, the route might be changed, and the final cost might be changed. An algorithm called greedy algorithm may solute this problem. The greedy algorithm is to divide the whole problem into many small portions and make every small portion to be optimal. The whole problem may be optimal.

This problem, the entire cost can be divided into three parts. The entire cost is equal to white blocks cost plus red blocks cost plus yellow blocks cost. And, no matter white or colored blocks, the fundamental cost is Ct* ΔT + Cf+*ΔF +Cc. Colored blocks extra costs are separate which can be considered later. Also, the colored blocks are not so many, they can hardly affect the entire cost.

The first step is to find the lowest cost of each white block ( Ct * ΔT + Cf * ΔF ), the constraint of it is Ct * ΔT + Cf * ΔT >= 25, So if white cost is 25, it is the lowest cost.
the next problem is to distribute the number, because each parameter is integer, the distribution for these four parameters is not hard to find out.
After finding the distribution, the ΔFa and ΔTa should be considered. The constraint of them is ΔFa+ΔTa >=10. if ΔFa + ΔTa > 10, the result is always greater than the combination of Δ Fa. + Δ Ta =10.If ΔFa=x while ΔTa=y, then no matter making x or y less can make ΔFa*Cf+ΔTa*Ct less. so letting left side equal to 10 is the best choice. Due to change these two variables will change the route. The greatest way is to try 20 times to find which combination is the best.

b. Results


After trying few times, the result came out. There are many results are the same value, the report shows only one set of data.
CF=16 CT=9 DF=1 DT=1 DFa=0 DTa=10

<img width="351" alt="截屏2021-10-26 12 41 53" src="https://user-images.githubusercontent.com/90883941/138810123-95e5c407-7ee3-4c94-8565-264251c4ce79.png">

The lowest cost is here.

<img width="325" alt="截屏2021-10-26 12 42 40" src="https://user-images.githubusercontent.com/90883941/138810181-3c716fd8-330e-48a5-9084-33cb0aefa540.png">

c. Discussion


The core of this methodology is greedy algorithm. About greedy algorithm, it has not a fixed format like Dijkstra, divide-and-conquer algorithm. It is more like a way of thinking. In this problem, it can reduce the times to try out the correct answer. So many people tried 20^6 times to find the answer. And python is not so efficient, by this way it will consume much extra time. The using of algorithm is always to help people to solve problem. 

## Task3
a. Methodology

The A-star path planning program can calculate the minimum cost and show the path on the screen. When considering the minus-cost area to reduce the cost of the aircraft given, we can first to find the condition of the minus-cost area. The condition is the area of minus-area is not greater than 16m^2 while the shape of the area is not limited. So, the best way of distributing the minus-cost area is to pave them under the path by a line. The minus-cost area does not affect the path when reducing the cost with 16 grid points in total. Each grid point is a slim cube If one side of the cube is parallel with the path, the reducing cost is less than the condition when its diagonal superposes the path. The cube cannot spin, so the path whose slope is 1 or -1 is the place to put 16 minus-cost grid points.

<img width="438" alt="截屏2021-10-26 15 13 17" src="https://user-images.githubusercontent.com/90883941/138830597-43797c42-efa9-4dca-ad4b-d79cb4c7c472.png">

b. Results


The aircraft configuration and cost is on the picture below.

<img width="204" alt="截屏2021-10-26 14 53 33" src="https://user-images.githubusercontent.com/90883941/138830538-579e16aa-37b3-44a6-868e-f98adee1c0b8.png">

<img width="333" alt="截屏2021-10-26 14 52 24" src="https://user-images.githubusercontent.com/90883941/138830557-4164c668-9f22-441b-ad62-6119c866d219.png">


After adding the minus-cost area, the reducing cost is 4*sqrt(2)*16 which approximates 90.51

The final cost approximates 3206.58.


c. Discussion

In this task, since the goal is simply to add a minus-cost area, so we instantly think of making 16 different grid points on all the slopes, so that we could maximize the reduction. And the core of solution is to realize the reducing cost is not the same when the path goes through the cube in different ways. After realizing this, it is not difficult to distribute the minus-cost area.




## Task4-1 Adding Checkpoints
### a. Methodology

This is an add-on for the Task1. Therefore, modify the main function of Task1 will be able to add the checkpoints.

**First, import math and matplotlib, also set up the show_animation function.**
```python
import math

import matplotlib.pyplot as plt

show_animation = True
```
**Second, imply the AStar Algorithm demo from [a_star.py](https://github.com/AtsushiSakai/PythonRobotics/blob/master/PathPlanning/AStar/a_star.py) .**
```python
class AStarPlanner:
......
```
**The most important part is modifying the main function.**
```python
def main():
    print(__file__ + " Start the A star algorithm demo with 2 checkpoints !!") # print simple notes

    # start and checkpoint 01 position
    sx = 0.0  # [m]
    sy = 0.0  # [m]
    gx = 17.0  # [m]
    gy = 30.0  # [m]
    grid_size = 1  # [m]
    robot_radius = 1.0  # [m]
    
    ox, oy = [], []
    for i in range(-10, 60): # draw the button border 
        ox.append(i)
        oy.append(-10.0)
    for i in range(-10, 60): # draw the right border
        ox.append(60.0)
        oy.append(i)
    for i in range(-10, 60): # draw the top border
        ox.append(i)
        oy.append(60.0)
    for i in range(-10, 60): # draw the left border
        ox.append(-10.0)
        oy.append(i)

    for i in range(-10, 50): # draw the free border
        ox.append(i)
        oy.append(10.0)

    for i in range(10, 60): # draw the free border
        ox.append(i)
        oy.append(40.0)
    
    # set fuel consuming area
    fc_x, fc_y = [], []
    for i in range(15, 30):
        for j in range(20, 40):
            fc_x.append(i)
            fc_y.append(j)
    
    # set time consuming area
    tc_x, tc_y = [], []
    for i in range(20, 35):
        for j in range(42, 55):
            tc_x.append(i)
            tc_y.append(j)

    if show_animation:  # pragma: no cover
        plt.plot(fc_x, fc_y, "oy") # plot the fuel consuming area
        plt.plot(tc_x, tc_y, "or") # plot the time consuming area
        plt.plot(ox, oy, ".k") # plot the obstacle
        plt.plot(0, 0, "or") # plot the start position 
        plt.plot(17,30, "og") # plot the checkpoint
        plt.plot(23,47, "ob") # plot the checkpoint
        plt.plot(50,50, "xk") # plot the end position
        plt.grid(True) # plot the grid to the plot panel
        plt.axis("equal") # set the same resolution for x and y axis 

    a_star = AStarPlanner(ox, oy, grid_size, robot_radius, fc_x, fc_y, tc_x, tc_y)
    rx, ry = a_star.planning(sx, sy, gx, gy)

    if show_animation:  # pragma: no cover
        plt.plot(rx, ry, "-k") # show the route 
        plt.pause(0.001) # pause 0.001 seconds
        plt.plot(0, 0, "or") # plot the start position 
        plt.plot(17,30, "og") # plot the checkpoint
        plt.plot(23,47, "ob") # plot the checkpoint
        plt.plot(50,50, "xk") # plot the end position

    # checkpoint 01 and checkpoint 02 position
    sx = 17.0  # [m]
    sy = 30.0  # [m]
    gx = 23.0  # [m]
    gy = 47.0  # [m]
    rx, ry = a_star.planning(sx, sy, gx, gy)

    if show_animation:  # pragma: no cover
        plt.plot(rx, ry, "-k") # show the route 
        plt.pause(0.001) # pause 0.001 seconds
        plt.plot(0, 0, "or") # plot the start position 
        plt.plot(17,30, "og") # plot the checkpoint
        plt.plot(23,47, "ob") # plot the checkpoint
        plt.plot(50,50, "xk") # plot the end position

    # checkpoint 01 and goal position
    sx = 23.0  # [m]
    sy = 47.0  # [m]
    gx = 50.0  # [m]
    gy = 50.0  # [m]
    rx, ry = a_star.planning(sx, sy, gx, gy)

    if show_animation:  # pragma: no cover
        plt.plot(rx, ry, "-k") # show the route 
        plt.pause(0.001) # pause 0.001 seconds
        plt.plot(0, 0, "or") # plot the start position 
        plt.plot(17,30, "og") # plot the checkpoint
        plt.plot(23,47, "ob") # plot the checkpoint
        plt.plot(50,50, "xk") # plot the end position
        plt.show() # show the plot
```
**At the end, call the main function to plot the graph.**
```python
if __name__ == '__main__':
    main()
```
### b. Results

<img width="500" height="450" src="https://github.com/Ronaldlo/first-project/blob/main/Task4.1%20Gif.gif">

### c. Discussion

This task simulated the reality flight path planning. In real life, an aircraft flight plan will include different waypoints to fly-by or flyover to define an area navigation route. Back to the coding practice of this task, the modified parts are setting the AStarPlanner in the separated route. The first route is that flying from the start point to checkpoint 1 which is in the fuel consuming area. The second route is that flying from checkpoint 1 to checkpoint 2 which is in a time-consuming area. The last route is flying from checkpoint 2 to the endpoint. Then, plot the points and routes with calling AStarPlanner one-by-one. 

## Task4-2 Changing Environment
### a. Methodology

**First, import math and matplotlib, also set up the show_animation function. Moreover, import the random**
```python
import math
import random
import matplotlib.pyplot as plt
```
**Second, imply the AStar Algorithm demo from [a_star.py](https://github.com/AtsushiSakai/PythonRobotics/blob/master/PathPlanning/AStar/a_star.py) but modify the get_motion_model to disable diagonal movements. For debugging, deleting time-consuming area and raelated variables is recommended**
```python
class AStarPlanner:
......
@staticmethod
    def get_motion_model(): # the cost of the surrounding 8 points
        # dx, dy, cost
        motion = [[1, 0, 1],
                  [0, 1, 1],
                  [-1, 0, 1],
                  [0, -1, 1]]
        return motion
``` 

**Third, define the main function again. **

```python
def main():
    print(__file__ + " Start the A star algorithm demo !!") # print simple notes


    ox, oy = [], []
    for i in range(-10, 60): # draw the button border 
        ox.append(i)
        oy.append(-10.0)
    for i in range(-10, 60): # draw the right border
        ox.append(60.0)
        oy.append(i)
    for i in range(-10, 60): # draw the top border
        ox.append(i)
        oy.append(60.0)
    for i in range(-10, 60): # draw the left border
        ox.append(-10.0)
        oy.append(i)
    
    # Only the fuel-consuming area remainsand generate it randomly with a fixed area (30x30)
    
    fc_x, fc_y = [], []
    r_fc_x = random.randrange(-9, 31) 
    r_fc_y = random.randrange(-9, 31) 
    for i in range(r_fc_x, r_fc_x+30):
        for j in range(r_fc_y, r_fc_y+30):
            fc_x.append(i)
            fc_y.append(j)
            
    # Diagonal movement is disabled, change parameter(s) so that the object could travel within one grid size
    
    grid_size = 1  
    robot_radius = 0
    
    # Destination and starting points aregenerated randomly with at least a 50-unit distance in-between
    
    while True:
        sx = random.randrange(-10, 59)  # [m]
        sy = random.randrange(-10, 59)  # [m]
        gx = random.randrange(-10, 59)  # [m]
        gy = random.randrange(-10, 59)  # [m]
        if (gx-sx) >= 50 or (sx-gx) >= 50 or (gy-sy) >= 50 or (sy-gy) >= 50:
            break
    
    # Obstacles are generated randomly with reasonable density
    
    for i in range(0,700): # The number of obstacles is around 700 will be reasonable
        g1=random.randrange(-9, 60)
        g2=random.randrange(-9, 60)
        if((abs(g1-sx)<=3 and abs(g2-sy)<=3 ) or (abs(g1-gx)<=3 and abs(g2-gy)<=3)):
            continue
        ox.append(g1)
        oy.append(g2)
        
    # Plotting of the fuel-consuming area would not cover the obstacles, and obstacles should not generate at/near the start and end point
    
    for i in range(0,700):
        g1=random.randrange(-9, 60)
        g2=random.randrange(-9, 60)
        if((abs(g1-sx)<=3 and abs(g2-sy)<=3 ) or (abs(g1-gx)<=3 and abs(g2-gy)<=3)):
            continue
        ox.append(g1)
        oy.append(g2)
    
    if show_animation:
        plt.plot(fc_x, fc_y, "oy")
        plt.plot(r_fc_x, r_fc_y)
        plt.plot(ox, oy, ".k")
        plt.grid(True)
        plt.axis("equal")

    a_star = AStarPlanner(ox, oy, grid_size, robot_radius, fc_x, fc_y)
    rx, ry = a_star.planning(sx, sy, gx, gy)

    if show_animation:
        plt.plot(rx, ry)
        plt.pause(0.001)
        plt.plot(sx, sy, "og")
        plt.plot(gx, gy, "xb")
        plt.show()
```
**At the end, call the main function to plot the graph.**
```python
if __name__ == '__main__':
    main()
```
### b. Results

**Extracting three sample simulations**   
* [Figure_1](https://github.com/Ronaldlo/first-project/blob/08a7933ef2c6ce009f65864a6412e788d2eb6249/Task4,2%20Figure_1%20Gif.gif)
<img width="500" height="450" src="https://github.com/Ronaldlo/first-project/blob/08a7933ef2c6ce009f65864a6412e788d2eb6249/Task4,2%20Figure_1%20Gif.gif">

* [Figure_2](https://github.com/Ronaldlo/first-project/blob/08a7933ef2c6ce009f65864a6412e788d2eb6249/Task4,2%20Figure_2%20Gif.gif)
<img width="500" height="450" src="https://github.com/Ronaldlo/first-project/blob/08a7933ef2c6ce009f65864a6412e788d2eb6249/Task4,2%20Figure_2%20Gif.gif">

* [Figure_3](https://github.com/Ronaldlo/first-project/blob/08a7933ef2c6ce009f65864a6412e788d2eb6249/Task%204.2%20Figure_3%20Gif.gif)  
<img width="500" height="450" src="https://github.com/Ronaldlo/first-project/blob/08a7933ef2c6ce009f65864a6412e788d2eb6249/Task%204.2%20Figure_3%20Gif.gif">

### c. Discussion

This task required advanced coding(python) skills to fulfill the requirement. The most important key of this task is random. Therefore, besides the number of obstacles and boundaries are settled. Other parameters should be coded to plot randomly. Moreover, this task is simulating a realistic environment. The potential obstacles are unpredictable in the real world, especially for a flying drone. The importance of the flexibility of the algorithm is shown via this task.   

## Task4-3 Comparing Algorithms

### a. Methodology & b. Disscussion

**Brief Background**

To understand these path planning algorithms better or easier, the concept of path planning should be introduced first. Imagine that we want to find a path from starting pose to a goal pose and if we are talking about a robot that moves along the ground, there may be three states that make up it's pose - x, y location and it's orientation. A path is a sequence of pose states that smoothly connect the start and the goal and determining this sequence is called path planning. In order to find an optimal path instead of building up a tree, which is used to find the goal with a cost that is low enough, through randomly wandering. So this is where path planning algorithms come in. They provide more efficient ways to build this tree. Starting with the search based methods that build up the tree by adding nodes in an ordered pattern. To accomplish this in practice is to start with a grid base map and go cell by cell and determine the cost or the distance the robot would have to go in order to reach the cell with is goal. Once we have covered every single cell in the grid the optimal path is simply the sequence of cells that produce the minimum cost at the goal. This will produce an optimal solution at least optimal at the resolution of the grid but you can see it would be computationally expensive since it's kind of a brute-force method of checking every possible node. So to improve this, researchers came up with a-star algorithm.

**AStar Algorithm Path Planning**

* [AStar](https://github.com/AAEfir6/first-project/blob/main/Task%204/Comparing_Algorithm/AStar.Algorithm.py)
```python
class AStarPlanner:
......
if __name__ == '__main__':
    main()
```
A-star Algorithm is still adds nodes in an ordered way but it does so by prioritizing the nodes that are more likely to produce the optimal path and searching they first. It does this by keeping track of some other heuristic like the straight-line distance from a node to the goal in addition to the cost of the node and sum of these two numbers is the absolute minimum cost of the path. A-star algorithm allows us to search through the nodes in a way that will get us to the goal without necessarily having to add every node into our tree. In fact, once we get to the goal we know that took the optimal path since every other path would have a cost plus distance to go that is greater than the path that we found.
```python
def verify_node(self, node):
        px = self.calc_grid_position(node.x, self.min_x)
        py = self.calc_grid_position(node.y, self.min_y)

        if px < self.min_x:
            return False
        elif py < self.min_y:
            return False
        elif px >= self.max_x:
            return False
        elif py >= self.max_y:
            return False
```
This showing how to decide the node to take for the final path.
```python
    @staticmethod
    def get_motion_model(): # the cost of the surrounding 8 points
        # dx, dy, cost
        motion = [[1, 0, 1],
                  [0, 1, 1],
                  [-1, 0, 1],
                  [0, -1, 1],
                  [-1, -1, math.sqrt(2)],
                  [-1, 1, math.sqrt(2)],
                  [1, -1, math.sqrt(2)],
                  [1, 1, math.sqrt(2)]] 
```
This showing the movements of robot.

However, this is a problem with a-star algorithm that it becomes very computationally expensive as the size and dimensions of the state space increases. We can imagine how the number of grid points grow exponentially as the number of dimensions increase which can slow everything down. Therefore, a-star algorithm tends to not be used for high dimensional state spaces, things like determining the path for multi-jointed robot manipulators or, for really large, low dimensional state spaces ones that might have millions or more grid cells.

For the coming up algorithm, d-star algorithm which stands for "Dynamic A* Search".

**DStar Algorithm Path Planning**

* [DStar](https://github.com/AAEfir6/first-project/blob/c4093c464f1013c315357f301f3510d7f3c85ace/Task%204/Comparing_Algorithm/DStar.py)
```python
class State:
......
if __name__ == '__main__':
    main()
``` 
It is similar to a-star algorithm but with it's own characteristics, replanning. D-star is also a search-based method but it aims to create a short path in real-time by incrementally reforming paths for the robot’s state as a new information is found. The robot will find a shortest path from its current coordinates to the goal coordinates under its acknowledgement of obstacles. When it observes new map information(unknown obstacles), it adds the information to its own map and, if necessary, replans a new shortest path from its current coordinates to the given goal coordinate. It repeats the process until it reaches the goal coordinates or determines that the goal coordinates cannot be reached. Using technical words to explain, A* and D* share general components of their set up meaning both have OPEN and CLOSE list. The difference between A* and D* is that D* has two additional lists: RAISE and LOWER. D-star algorithm is more efficient than a-star in expansive and complex environments since it avoids high computational costs of backtracking, and it is optimal and complete. 
However, it's downside might be the amount of time it takes to do the calculations and if a path has to be re-planning that lengthens the amount of time it takes to do one simulation.

For another type of method, sampling-based method is introduced - Probabilistic RoadMap (RPM).

**Probabilistic RoadMap (RPM) Path Planning**

* [Probabilistic RoadMap](https://github.com/AAEfir6/first-project/blob/main/Task%204/Comparing_Algorithm/PRM.py)
```python
class Node:
......
if __name__ == '__main__':
    main()
```
To understand how this algorithm works, it is helpful to realize that in most map, there are sections where a path could continue in a straight direction for some distance before it needs to make a turn. With a-star, we have to calculate every single grid cell between the start and goal points, so multiple nodes in the tree. However, if we only checked the far-distant node and there weren't any obstacles in the way then we could calculate the straight line cost for just the node which is before turning. This reduces the total number of nodes and the total number of calculations. So the question becomes how do we pick the location of these sparse nodes so that we still reach the goal. The answer is to sample them. Once the nodes are sampled, nodes are connected to the nearest k neighbors to create a graph structure. The graph structure can then be queried for paths between any two points in the graph. One benefit of PRM is that once a graph is constructed, it can be queried repeatedly for paths without having to construct a new graph. This algorithm is very useful but, it does not give the optimal solution every time. Consider a configuration space with a large number of obstacles situated very close to each other. Assume the gap between two obstacles is very narrow. Recall, that our system generates nodes randomly. Due to this, the probability of generating nodes between those gaps is very small. The system might generate nodes in that region if we increase the number of iterations. You might think that increasing the number of iterations solves the problem, but it is not the case. When the system fails to generate a path for such configurations of the space, we wouldn’t know whether it is because the path does not exist or the number of iterations is less for that environment. This is the only drawback of this algorithm. It does not paint a clear picture for us in event of failure.

### c. Ressults

* [AStar](https://github.com/AAEfir6/first-project/blob/main/Task%204/Comparing_Algorithm/AStar.Algorithm.py)
<img width="500" height="450" src="https://github.com/Ronaldlo/first-project/blob/3185ec432a9c228a58aef47bd3dad133c2cf4728/Task%204.3%20AStar.gif">


* [DStar](https://github.com/AAEfir6/first-project/blob/c4093c464f1013c315357f301f3510d7f3c85ace/Task%204/Comparing_Algorithm/DStar.py)
<img width="500" height="450" src="https://github.com/Ronaldlo/first-project/blob/3185ec432a9c228a58aef47bd3dad133c2cf4728/Task%204.3%20DStar.gif">


* [Probabilistic RoadMap](https://github.com/AAEfir6/first-project/blob/main/Task%204/Comparing_Algorithm/PRM.py)
<img width="500" height="450" src="https://github.com/Ronaldlo/first-project/blob/3185ec432a9c228a58aef47bd3dad133c2cf4728/Task%204.3%20PRM.gif">

## Reflective Essay

a. Member 1(YAN Zhengyang)

The freshman project is a little difficult but valuable to me. It required us to learn the A-star path planning algorithm. Though we never got into this field, we were still enthusiastic to challenge ourselves.
I think it is helpful to use GitHub. By using this, I know how to establish a repository and work together with others. And through GitHub, I can get advanced information from all over the world. Then interchange thoughts with many people. During handling these tasks, we distributed several tasks to one or two persons. And I was responsible for the task2-2 and task3. It was not easy for me. Because of the lack of mathematics knowledge, I needed to learn new knowledge to solve them. In this procedure, I have learned how to get new knowledge on my own and to get a proper way to handle difficulties. 
I extremely appreciate that I can meet such great teammates. They all finished their own tasks punctually. And during we were doing the tasks, we helped each other and shared our thoughts. Through this, it strikes me that partnership is vital to achieve success. We learned how to corporate with others. As I see it, this is more important than the knowledge I have learned during the project.


<br>b. Member 2 (Leung Yi Him)

<br> Before doing this project, I am unfamiliar with aviation stuff and using the git hub to build the algorithm. And I didn’t expect there to be so many codes we need to develop and calculate so many math equations. But after I finished the project, I think the point I worried about is not a big deal, Since I can learn it from the internet. Apart from the knowledge I learned from the project, it lets me increase my interest in aviation.
<br><br>
When I started my project, I felt frightened about the content and the groupmate since there is the hybrid mode teaching this semester. Some of our groupmate was not inside the classroom when the first lesson. Fortunately, I can use social media to contact all the groupmate successfully. In the second project lesson, we can group all the groupmate to be involved in our project. No need to facing the delay of the zoom, not responding from the online call, daydreaming via online meeting. Moreover, some of my groupmates is good at coding and mathematics. And we can distribute the task to everyone according to their ability. For me, I am the teammate who is setting up the flight environment for our group. Initially, I don’t know to build our map by myself. But after my groupmate invested the map with me, we finally set up the environment for the task.
<br><br>
To Sum up, the most memorable part I learnt is the markdown language and the collaboration of the report. Because it is another method that I can build a document or HTML, and I can use GitHub to edit and run the code together. Before I learn this skill, I only can use google doc and notepad++ to send files to each other and have a lot of versions of the documents. But after I learn how to use those tools, I think it is a very good invention for a team to work together. Overall, this project let me learn many new things, no matter the aviation and the programming areas.
<br>

<br>c. Member 3(Yulong Wang Walton)
  
  When I choose the AAE project I wish to learn something about coding because I have not coded any program before.With the happy mind I walked in the classroom W502g.
  
  But things went not very smooth because Prof. Hsu told us that we need to do everything by ourselves and he would guide us if we have any question.As a quiet student I really don’t want to talk with any stranger.So I just learnt to do everything by myself.The process was pretty tough and sometimes I even wanted to give up especially at the beginning of the task—I did not know how to attend our group’s Github project.That made me extremely sad.However,thanks to the help of Nikkie I finally joined the group project and got down to learning coding.I searched on the Internet to find anything I want and then applied the knowledge to the project.Then came to the real challenge—task 2-1.
  
  For task 2-1 I have lot to say.Generally speaking,it is the most challenging task when I entered PolyU.I do not know how to design a programming to calculate the minimum cost—but I held the firm belief that there must be other methods to solve the problem.I searched on the Internet again but found nothing relevant.So I searched help from other classmates.And they told me that I could use the knowledge learnt from high school.So I walked back to home and thought about it again and again.Fortunately,I found the ket—Linear Programming.I was excited when I was doing this “math” problem.And afterwards,everything seemed better.
  
  To conclusion,the freshman project made me learn a lot.Thanks to Prof. Hsu’s teaching method because I not only learnt how to code a program but also learnt how to learn in a new way.In the end,thanks for my devoted teammate.


<br>d. Member 4
<br>e. Member 5

## References
Ahmad, Z., Ullah, F., Tran, C., & Lee, S. (2017). Efficient energy flight path
planning algorithm using 3-d visibility roadmap for small unmanned aerial
vehicle. International Journal of Aerospace Engineering, 2017.
Stentz, Anthony (1994), "Optimal and Efficient Path Planning for Partially-Known Environments", Proceedings of the International Conference on Robotics and Automation
