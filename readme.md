
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
      <a href="#Task21">Task 2.1: Methodology, Results and Discussion</a>
    </li>
    <li>
      <a href="#Task22">Task 2.2: Methodology, Results and Discussion</a>
    </li>
    <li>
      <a href="#Task3">Task 3: Methodology, Results and Discussion</a>
    </li>
    <li>
      <a href="#Task4">Task 4: Methodology, Results and Discussion</a>
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
**General Inquiry**

Dr Li-Ta Hsu -  lt.hsu@polyu.edu.hk - https://github.com/qmohsu

Dr Weisong Wen -  welson.wen@polyu.edu.hk - https://github.com/weisongwen


**Assistance on Your Project**

*Group 1-3*

Miss Hui Yi (Queenie) HO - hiu-yi.ho@connect.polyu.hk - https://github.com/queenie-ho

*Group 4-6*

Miss Yan Tung (Nikkie) LEUNG - yan-tung.leung@connect.polyu.hk - https://github.com/tungtungyan

*Group 7-10*

Mr Man Hin (Melvin) CHENG - manhin.cheng@connect.polyu.hk - https://github.com/Melvincheng0830

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

## Task2.1
<br>a. Methodology

Linear programming—We treat C(T)=x and C(F)=y.Then We got four inequalities and drew them all in the same x-y coordinate(see the black lines),after that we could find there is a common area which is surrounded by the four lines(see the red area).On the other hand because C=x*delta_F+y*delta_T+C_c. Delta_F=delta_T=5 and C_c=a constant.Therefore C=5(x+y)+C_c.We let C(min)=Z.Then simplify it we got y>=0.2(Z-C_c)-x.It means a clust of parallel lines and we drew some of them in the former coordinate(see the blue lines).The minimum C where it is must be at the border of the red area and we found that when x=20 and y=20 comes the minimum C.
![image](https://user-images.githubusercontent.com/91596396/138546153-c3914fcb-3af8-422e-ac05-2f794d9e91fc.png)

b. Results

![image](https://user-images.githubusercontent.com/91596396/138546170-5d486cf2-d013-464e-8c5e-f96f7ed66c34.png)



![image](https://user-images.githubusercontent.com/91596396/138546174-ea40ec34-d80b-4d34-8d4f-5a5526accc11.png)

c. Discussion

This method（Linear Programming）only can be applied in Linear equation in 2 unknowns.So it is not a universal method to solve many problems.However,it is a easy way to solve Task 2-1 with just a pen and a piece of paper.We got to know from the website that there is a more convenient way to deal with the problem by using computer coding.Maybe we will try it next time.
![image](https://user-images.githubusercontent.com/91596396/138546191-5946d538-7718-43bf-96d6-3bd5e631c92c.png)


## Task2.2
a. Methodology
There are six variables, and four constraints need to be considered.

<img width="314" alt="截屏2021-10-26 12 38 24" src="https://user-images.githubusercontent.com/90883941/138809863-4e6a2741-a2f5-48f4-b164-d97d4c51d041.png">


When a parameter is changed, the route might be changed, and the final cost might be changed. An algorithm called greedy algorithm may solute this problem. The greedy algorithm is to divide the whole problem into many small portions and make every small portion to be optimal. The whole problem may be optimal.

This problem, the entire cost can be divided into three parts. The entire cost is equal to white blocks cost plus red blocks cost plus yellow blocks cost. And, no matter white or colored blocks, the fundamental cost is Ct* ΔT + Cf+ ΔF +Cc. Colored blocks extra costs are separate which can be considered later. Also, the colored blocks are not so many, they can hardly affect the entire cost.

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




## Task4
### Task4.1 Adding checkpoints

### a. Methodology

This is an add-on for the Task1. Therefore, modify the main function of Task1 will be able to add the checkpoints.

**First, import math and matplotlib, also set up the show_animation function.**
```python
import math

import matplotlib.pyplot as plt

show_animation = True
```
**Second, imply the AStar Algorithm demo.**
```python
class AStarPlanner:

    def __init__(self, ox, oy, resolution, rr, fc_x, fc_y, tc_x, tc_y):
        """
        Initialize grid map for a star planning

        ox: x position list of Obstacles [m]
        oy: y position list of Obstacles [m]
        resolution: grid resolution [m]
        rr: robot radius[m]
        """

        self.resolution = resolution # get resolution of the grid
        self.rr = rr # robot radis
        self.min_x, self.min_y = 0, 0
        self.max_x, self.max_y = 0, 0
        self.obstacle_map = None
        self.x_width, self.y_width = 0, 0
        self.motion = self.get_motion_model() # motion model for grid search expansion
        self.calc_obstacle_map(ox, oy)

        self.fc_x = fc_x
        self.fc_y = fc_y
        self.tc_x = tc_x
        self.tc_y = tc_y

        ############you could modify the setup here for different aircraft models (based on the lecture slide) ##########################
        self.C_F = 1
        self.Delta_F = 1
        self.C_T = 2
        self.Delta_T = 5
        self.C_C = 10
        
        self.Delta_F_A = 2 # additional fuel
        self.Delta_T_A = 5 # additional time 
        
        

        self.costPerGrid = self.C_F * self.Delta_F + self.C_T * self.Delta_T + self.C_C

        print("PolyU-A380 cost part1-> ", self.C_F * (self.Delta_F + self.Delta_F_A) )
        print("PolyU-A380 cost part2-> ", self.C_T * (self.Delta_T + self.Delta_T_A) )
        print("PolyU-A380 cost part3-> ", self.C_C )

    class Node: # definition of a sinle node
        def __init__(self, x, y, cost, parent_index):
            self.x = x  # index of grid
            self.y = y  # index of grid
            self.cost = cost
            self.parent_index = parent_index

        def __str__(self):
            return str(self.x) + "," + str(self.y) + "," + str(
                self.cost) + "," + str(self.parent_index)

    def planning(self, sx, sy, gx, gy):
        """
        A star path search

        input:
            s_x: start x position [m]
            s_y: start y position [m]
            gx: goal x position [m]
            gy: goal y position [m]

        output:
            rx: x position list of the final path
            ry: y position list of the final path
        """

        start_node = self.Node(self.calc_xy_index(sx, self.min_x), # calculate the index based on given position
                               self.calc_xy_index(sy, self.min_y), 0.0, -1) # set cost zero, set parent index -1
        goal_node = self.Node(self.calc_xy_index(gx, self.min_x), # calculate the index based on given position
                              self.calc_xy_index(gy, self.min_y), 0.0, -1)

        open_set, closed_set = dict(), dict() # open_set: node not been tranversed yet. closed_set: node have been tranversed already
        open_set[self.calc_grid_index(start_node)] = start_node # node index is the grid index

        while 1:
            if len(open_set) == 0:
                print("Open set is empty..")
                break

            c_id = min(
                open_set,
                key=lambda o: open_set[o].cost + self.calc_heuristic(self, goal_node,
                                                                     open_set[
                                                                         o])) # g(n) and h(n): calculate the distance between the goal node and openset
            current = open_set[c_id]

            # show graph
            if show_animation:  # pragma: no cover
                plt.plot(self.calc_grid_position(current.x, self.min_x),
                         self.calc_grid_position(current.y, self.min_y), "xc")
                # for stopping simulation with the esc key.
                plt.gcf().canvas.mpl_connect('key_release_event',
                                             lambda event: [exit(
                                                 0) if event.key == 'escape' else None])
                if len(closed_set.keys()) % 10 == 0:
                    plt.pause(0.001)

            # reaching goal
            if current.x == goal_node.x and current.y == goal_node.y:
                print("Find goal with cost of -> ",current.cost )
                goal_node.parent_index = current.parent_index
                goal_node.cost = current.cost
                break

            # Remove the item from the open set
            del open_set[c_id]

            # Add it to the closed set
            closed_set[c_id] = current

            # print(len(closed_set))

            # expand_grid search grid based on motion model
            for i, _ in enumerate(self.motion): # tranverse the motion matrix
                node = self.Node(current.x + self.motion[i][0],
                                 current.y + self.motion[i][1],
                                 current.cost + self.motion[i][2] * self.costPerGrid, c_id)
                
                ## add more cost in time-consuming area
                if self.calc_grid_position(node.x, self.min_x) in self.tc_x:
                    if self.calc_grid_position(node.y, self.min_y) in self.tc_y:
                        # print("time consuming area!!")
                        node.cost = node.cost + self.Delta_T_A * self.motion[i][2]
                
                # add more cost in fuel-consuming area
                if self.calc_grid_position(node.x, self.min_x) in self.fc_x:
                    if self.calc_grid_position(node.y, self.min_y) in self.fc_y:
                        # print("fuel consuming area!!")
                        node.cost = node.cost + self.Delta_F_A * self.motion[i][2]
                    # print()
                
                n_id = self.calc_grid_index(node)

                # If the node is not safe, do nothing
                if not self.verify_node(node):
                    continue

                if n_id in closed_set:
                    continue

                if n_id not in open_set:
                    open_set[n_id] = node  # discovered a new node
                else:
                    if open_set[n_id].cost > node.cost:
                        # This path is the best until now. record it
                        open_set[n_id] = node

        rx, ry = self.calc_final_path(goal_node, closed_set)
        # print(len(closed_set))
        # print(len(open_set))

        return rx, ry

    def calc_final_path(self, goal_node, closed_set):
        # generate final course
        rx, ry = [self.calc_grid_position(goal_node.x, self.min_x)], [
            self.calc_grid_position(goal_node.y, self.min_y)] # save the goal node as the first point
        parent_index = goal_node.parent_index
        while parent_index != -1:
            n = closed_set[parent_index]
            rx.append(self.calc_grid_position(n.x, self.min_x))
            ry.append(self.calc_grid_position(n.y, self.min_y))
            parent_index = n.parent_index

        return rx, ry

    @staticmethod
    def calc_heuristic(self, n1, n2):
        w = 1.0  # weight of heuristic
        d = w * math.hypot(n1.x - n2.x, n1.y - n2.y)
        d = d * self.costPerGrid
        return d
    
    def calc_heuristic_maldis(n1, n2):
        w = 1.0  # weight of heuristic
        dx = w * math.abs(n1.x - n2.x)
        dy = w *math.abs(n1.y - n2.y)
        return dx + dy

    def calc_grid_position(self, index, min_position):
        """
        calc grid position

        :param index:
        :param min_position:
        :return:
        """
        pos = index * self.resolution + min_position
        return pos

    def calc_xy_index(self, position, min_pos):
        return round((position - min_pos) / self.resolution)

    def calc_grid_index(self, node):
        return (node.y - self.min_y) * self.x_width + (node.x - self.min_x) 

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

        # collision check
        if self.obstacle_map[node.x][node.y]:
            return False

        return True

    def calc_obstacle_map(self, ox, oy):

        self.min_x = round(min(ox))
        self.min_y = round(min(oy))
        self.max_x = round(max(ox))
        self.max_y = round(max(oy))
        print("min_x:", self.min_x)
        print("min_y:", self.min_y)
        print("max_x:", self.max_x)
        print("max_y:", self.max_y)

        self.x_width = round((self.max_x - self.min_x) / self.resolution)
        self.y_width = round((self.max_y - self.min_y) / self.resolution)
        print("x_width:", self.x_width)
        print("y_width:", self.y_width)

        # obstacle map generation
        self.obstacle_map = [[False for _ in range(self.y_width)]
                             for _ in range(self.x_width)] # allocate memory
        for ix in range(self.x_width):
            x = self.calc_grid_position(ix, self.min_x) # grid position calculation (x,y)
            for iy in range(self.y_width):
                y = self.calc_grid_position(iy, self.min_y)
                for iox, ioy in zip(ox, oy): # Python’s zip() function creates an iterator that will aggregate elements from two or more iterables. 
                    d = math.hypot(iox - x, ioy - y) # The math. hypot() method finds the Euclidean norm
                    if d <= self.rr:
                        self.obstacle_map[ix][iy] = True # the griid is is occupied by the obstacle
                        break

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

        return motion

```
**The most important part is modifying the main function.**
```python
def main():
    print(__file__ + " Start the A star algorithm demo with 2 checkpoints !!") # print simple notes

    # start and goal position
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
<img width="500" height="450" src="https://github.com/Ronaldlo/first-project/blob/main/Task4.1%20Fig.png">
<img width="500" height="450" src="https://github.com/Ronaldlo/first-project/blob/main/Task4.1%20Gif.gif">

### c. Discussion

### Task 4.2 Changing Environment

### a. Methodology

### b. Results

### c. Discussion

## Reflective Essay

a. Member 1
<br>
<br>b. Member 2
<br>c. Member 3
<br>d. Member 4
<br>e. Member 5

## References
Ahmad, Z., Ullah, F., Tran, C., & Lee, S. (2017). Efficient energy flight path
planning algorithm using 3-d visibility roadmap for small unmanned aerial
vehicle. International Journal of Aerospace Engineering, 2017.
For your self-learning https://www.polyu.edu.hk/aae/internal/studentresources/
PolyU AAE Endnote tutorial
https://www.youtube.com/watch?v=DP1bpnYRKxk
PolyU AAE report formatting tutorial
https://www.youtube.com/watch?v=p2GaOD_Ca1Y
