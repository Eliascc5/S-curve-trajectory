# S-curve-trajectory

S - curve or <b>7-segment</b> : a modification to the trapezoidal profile


<p align="center">
<img src="/img/s_profile.png" alt="Graph"
	title="Trajectory" width="200" height="230" />
</p>

We use  the following general forms for $q's$,$\dot{q}'s$,$\ddot{q}'s$and$ $\dddot{q}'s$: 

$$\dddot{q_{i}(t)}=a_{i}$$

$$\ddot{q_{i}(t)=}a_{i}t+b_{i}$$

$$\dot{q_{i}(t)}=\frac{a_{i}}{2}t^{2}+b_{i}t+c_{i}$$

$$q_{i}(t)=\frac{a_{i}}{6}t^{3}+\frac{b_{i}}{2}t^{2}+c_{i}t+d_{i}$$

$$i=1,2,3,4,5,6,7$$


Maximum $ \dot{q}$ is given by: $v_{max}$

Maximum $ \ddot{q}$ is given by: $a_{max}$

Maximum $ \dddot{q}$ is given by: $j_{max}$


-$q$ is zero at the begining $(d_1=0)$ and it is qf at the end of the motion$\quad (d_7=q_f)$


-$\dot{q}$ is zero at the begining $(b_1=0)$ and end of motion.

We assume $t_0=0$ and $t_f=T$ which is given by :  $T=\frac{a_{max}}{j_{max}}+\frac{v_{max}}{a_{max}}+\frac{q_{f}}{v_{max}}$

-Time points $t_1,t_3$ are calculated by the following  equations and $t_2=t_3-t_1$

$t_{1}=\frac{a_{max}}{j_{max}}$ $;\qquad$ $t_{3}=\frac{a_{max}}{j_{max}}+\frac{v_{max}}{a_{max}}<\frac{T}{2}$



-Symmetry also given us:

$t_{4}=T-t_{3}$ $;\quad$ $t_{5}=T-t_{2}$ $;\quad$ $t_{6}=T-t_{1}$

-We also use :

$a_{7}=a_{1}=j_{max}$ $;\quad$ $a_{5}=a_{3}=-j_{max}$ $;\quad$ $a_{6}=a_{2}=a_{4}=0$ $;\quad$ $b_{2}=-b_{6}=a_{max}$ $;\quad$ $b_{4}=0$ $;\quad$ $c_{4}=v_{max}$

-We use continuity conditions and smoothness conditions at points to find the unknown coefficients: $(b_3,b_5,b_7c_2,c_3,c_5,c_6,c_7,d_2,d_3,d_4,d_5,d_6,d_7)$
