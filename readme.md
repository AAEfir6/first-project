
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
To finish task 1, the group should modified the code to match the map was given to each group. Then test the aeroplane with different parameters in the source code to find the minimum achievable cost from those 4 aeroplanes were given.
![螢幕擷取畫面 2021-10-22 112618](https://user-images.githubusercontent.com/85985312/138388655-76fe86d4-d02c-4459-b05e-30cd6e492fbc.png)<br>
<br>b. Results
<br>c. Discussion

## Task21
a. Methodology

Linear programming—We treat C(T)=x and C(F)=y.Then We got four inequalities and drew them all in the same x-y coordinate(see the black lines),after that we could find there is a common area which is surrounded by the four lines(see the red area).On the other hand because C=x*delta_F+y*delta_T+C_c. Delta_F=delta_T=5 and C_c=a constant.Therefore C=5(x+y)+C_c.We let C(min)=Z.Then simplify it we got y>=0.2(Z-C_c)-x.It means a clust of parallel lines and we drew some of them in the former coordinate(see the blue lines).The minimum C where it is must be at the border of the red area and we found that when x=20 and y=20 comes the minimum C.
![image](https://user-images.githubusercontent.com/91596396/138546153-c3914fcb-3af8-422e-ac05-2f794d9e91fc.png)

b. Results


![image](https://user-images.githubusercontent.com/91596396/138546170-5d486cf2-d013-464e-8c5e-f96f7ed66c34.png)



![image](https://user-images.githubusercontent.com/91596396/138546174-ea40ec34-d80b-4d34-8d4f-5a5526accc11.png)

c. Discussion

This method（Linear Programming）only can be applied in Linear equation in 2 unknowns.So it is not a universal method to solve many problems.However,it is a easy way to solve Task 2-1 with just a pen and a piece of paper.We got to know from the website that there is a more convenient way to deal with the problem by using computer coding.Maybe we will try it next time.
![image](https://user-images.githubusercontent.com/91596396/138546191-5946d538-7718-43bf-96d6-3bd5e631c92c.png)


## Task22
a. Methodology
There are six variables, and four constraints need to be considered.

When a parameter is changed, the route might be changed, and the final cost might be changed. An algorithm called greedy algorithm may solute this problem. The greedy algorithm is to divide the whole problem into many small portions and make every small portion to be optimal. The whole problem may be optimal.

This problem, the entire cost can be divided into three parts. The entire cost is equal to white blocks cost plus red blocks cost plus yellow blocks cost. And, no matter white or colored blocks, the fundamental cost is Ct* ΔT + Cf+ ΔF +Cc. Colored blocks extra costs are separate which can be considered later. Also, the colored blocks are not so many, they can hardly affect the entire cost.

The first step is to find the lowest cost of each white block ( Ct * ΔT + Cf * ΔF ), the constraint of it is Ct * ΔT + Cf * ΔT >= 25, So if white cost is 25, it is the lowest cost.
the next problem is to distribute the number, because each parameter is integer, the distribution for these four parameters is not hard to find out.
After finding the distribution, the ΔFa and ΔTa should be considered. The constraint of them is ΔFa+ΔTa >=10. if ΔFa + ΔTa > 10, the result is always greater than the combination of Δ Fa. + Δ Ta =10.If ΔFa=x while ΔTa=y, then no matter making x or y less can make ΔFa*Cf+ΔTa*Ct less. so letting left side equal to 10 is the best choice. Due to change these two variables will change the route. The greatest way is to try 20 times to find which combination is the best.

b. Results


After trying few times, the result came out. There are many results are the same value, the report shows only one set of data.
CF=16 CT=9 DF=1 DT=1 DFa=0 DTa=0
The lowest cost is 5635.702161277668.

c. Discussion


The core of this methodology is greedy algorithm. About greedy algorithm, it has not a fixed format like Dijkstra, divide-and-conquer algorithm. It is more like a way of thinking. In this problem, it can reduce the times to try out the correct answer. So many people tried 20^6 times to find the answer. And python is not so efficient, by this way it will consume much extra time. The using of algorithm is always to help people to solve problem. 

## Task3
a. Methodology
b. Results
c. Discussion

## Task4
a. Methodology
b. Results

## Reflective Essay

a. Member 1
b. Member 2
c. Member 3
d. Member 4
e. Member 5

## References
Ahmad, Z., Ullah, F., Tran, C., & Lee, S. (2017). Efficient energy flight path
planning algorithm using 3-d visibility roadmap for small unmanned aerial
vehicle. International Journal of Aerospace Engineering, 2017.
For your self-learning https://www.polyu.edu.hk/aae/internal/studentresources/
PolyU AAE Endnote tutorial
https://www.youtube.com/watch?v=DP1bpnYRKxk
PolyU AAE report formatting tutorial
https://www.youtube.com/watch?v=p2GaOD_Ca1Y
