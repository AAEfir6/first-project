
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
a. Methodology
b. Results

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
