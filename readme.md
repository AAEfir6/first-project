
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
The objective in this task is to find the flight route with the minimum cost which can let the plane fly to the final destination.
b. Results
c. Discussion

## Task21
a. Methodology
b. asdfsadfasdfalsdflkajdslfkjalskdjfljsdfkllajdflkjlskljf
c. Discussion

## Task22
a. Methodology
There are six variables, and four constraints need to be considered.

When a parameter is changed, the route might be changed, and the final cost might be changed. An algorithm called greedy algorithm may solute this problem. The greedy algorithm is to divide the whole problem into many small portions and make every small portion to be optimal. The whole problem may be optimal.
This problem, the entire cost can be divided into three parts. The entire cost is equal to white blocks cost plus red blocks cost plus yellow blocks cost. And, no matter white or colored blocks, the fundamental cost is Ct* ΔT + Cf+ ΔF +Cc. Colored blocks extra costs are separate which can be considered later. Also, the colored blocks are not so many, they can hardly affect the entire cost.
The first step is to find the lowest cost of each white block ( Ct * ΔT + Cf * ΔF ), the constraint of it is Ct * ΔT + Cf * ΔT >= 25, So if white cost is 25, it is the lowest cost.
the next problem is to distribute the number, because each parameter is integer, the distribution for these four parameters is not hard to find out.
After finding the distribution, the ΔFa and ΔTa should be considered. The constraint of them is ΔFa+ΔTa >=10. if ΔFa + ΔTa > 10, the result is always greater than the combination of Δ Fa. + Δ Ta =10.If ΔFa=x while ΔTa=y, then no matter making x or y less can make ΔFa*Cf+ΔTa*Ct less. so letting left side equal to 10 is the best choice. Due to change these two variables will change the route. The greatest way is to try 20 times to find which combination is the best.

b. Results
c. Discussion

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
