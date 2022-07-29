# -*- coding: utf-8 -*-
"""
Created on Mon Jul  4 12:19:59 2022

@author: EliasC
"""

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import math
import sys
import time
#Jerk = 2*(amax**2/vmax)

t_inicial=time.time()
sns.set_theme()

jmax = 30

vmax = 10
vi = 7.5
vf = 0
amax = 10


qi=  0
qf = 10


if (qf < 0):
       
    amax = -amax
    vmax = -vmax
    jmax = -jmax
    
Tjaux= min(math.sqrt(abs(vf-vi)/jmax),amax/jmax)


if Tjaux<amax/jmax:
    if qf-qi > Tjaux*(vi+vf):
        print("the trajectory is feasible")
    else:
        print("the trajectory is NOT feasible")
        
elif Tjaux == amax/jmax:
    if qf-qi > 0.5*(vi+vf)*(Tjaux+abs(vi+vf)/amax):
        print("the trajectory is feasible")
    else:
        print("the trajectory is NOT feasible")

#Phase 1: acceleration
if (vmax-vi)*jmax < amax**2:
    print("amax is NOT reached")
    
    Tj1=math.sqrt(abs(vmax-vi)/jmax)
    Ta=Tj1*2
else:
    print("amax is reached")
    Tj1=amax/jmax
    Ta=Tj1+(vmax-vi)/amax
    
#Phase 3: Desacceleration
amin = -amax
if (vmax-vf)*jmax < amax**2:
    print("amin is NOT reached")
    
    Tj2=math.sqrt(abs(vmax-vf)/jmax)
    Td=Tj2*2
else:
    print("amin is reached")
    Tj2=amax/jmax
    Td=Tj2+(vmax-vf)/amax


Tv=(qf-qi)/vmax - Ta/2*(1+vi/vmax)-Td/2*(1+vf/vmax)

if Tv>0:
    print("the max velocity is reached")
else:
    print("CASE 2")
    print("In this case vmax is NOT reached, so Tv=0")
    Tj1=amax/jmax
    Tj2=Tj1
    Tj=Tj1
    delta = (pow(amax,4)/pow(jmax,2))+2*(pow(vi,2)+pow(vf,2))+amax*(4*(qf-qi)-2*(amax/jmax)*(vi+vf))
    Ta=((pow(amax,2)/jmax)-2*vi+math.sqrt(delta))/(2*amax)
    Td=((pow(amax,2)/jmax)-2*vf+math.sqrt(delta))/(2*amax)
    Tv=0
    i=0
    
    if Ta<2*Tj or Td<2*Tj:
        print("entre")
        while not(Ta>2*Tj and Td>2*Tj):
            amax=amax*0.99
            Tj=amax/jmax
            delta = (pow(amax,4)/pow(jmax,2))+2*(pow(vi,2)+pow(vf,2))+amax*(4*(qf-qi)-2*(amax/jmax)*(vi+vf))
            Ta=((pow(amax,2)/jmax)-2*vi+math.sqrt(delta))/(2*amax)
            Td=((pow(amax,2)/jmax)-2*vf+math.sqrt(delta))/(2*amax)
            
            print(f'{i}',amax)
            i+=1
 
            if Ta<0:
                Ta=0
                Tj1=0
                Td=2*((qf-qi)/(vf+vi))
                Tj2=(jmax*(qf-qi)-math.sqrt(jmax*(jmax*(pow(qf-qi,2))+ pow(vf+vi,2)*(vf-vi))))/(jmax*(vf+vi))
                break
        

#%%
print(amax)
print(Ta)
print(Td)
print(Tv)
print(Tj1)
print(Tj2)

t1=Tj1
T=Ta+Td+Tv

t3=Ta
t2=t3-t1

t4=T-Td

t5=t4+Tj2
t6=t5+Tj2

a1=jmax
a2=0
a3=-jmax
a4=0
a5=-jmax
a6=0
a7=jmax


b1=0
b2=amax
b3=amax+jmax*t2
b4=0
b5=jmax*t4
b6=-amax
b7=-amax-jmax*t6

c1=0
c2=((a1*t1**2)/2+b1*t1+c1)-((a2*t1**2)/2+b2*t1)
c3=((a2*t2**2)/2+b2*t2+c2)-((a3*t2**2)/2+b3*t2)
c4=((a3*t3**2)/2+b3*t3+c3)-((a4*t3**2)/2+b4*t3)
c5=((a4*t4**2)/2+b4*t4+c4)-((a5*t4**2)/2+b5*t4)
c6=((a5*t5**2)/2+b5*t5+c5)-((a6*t5**2)/2+b6*t5)
c7=((a6*t6**2)/2+b6*t6+c6)-((a7*t6**2)/2+b7*t6)

d1=0
d2=((a1*t1**3)/6+(b1*t1**2)/2+c1*t1+d1)-((a2*t1**3)/6+(b2*t1**2)/2+c2*t1)
d3=((a2*t2**3)/6+(b2*t2**2)/2+c2*t2+d2)-((a3*t2**3)/6+(b3*t2**2)/2+c3*t2)
d4=((a3*t3**3)/6+(b3*t3**2)/2+c3*t3+d3)-((a4*t3**3)/6+(b4*t3**2)/2+c4*t3)
d5=((a4*t4**3)/6+(b4*t4**2)/2+c4*t4+d4)-((a5*t4**3)/6+(b5*t4**2)/2+c5*t4)
d6=((a5*t5**3)/6+(b5*t5**2)/2+c5*t5+d5)-((a6*t5**3)/6+(b6*t5**2)/2+c6*t5)
d7=((a6*t6**3)/6+(b6*t6**2)/2+c6*t6+d6)-((a7*t6**3)/6+(b7*t6**2)/2+c7*t6)

N=100
t=np.linspace(0,T,N)

ind1 = [index for index,value in enumerate(t) if value<=t1]

ind2 = [index for index,value in enumerate(t) if value<=t2]
ind2 = [idx for idx in ind2 if idx not in ind1]

ind3 = [index for index,value in enumerate(t) if value<=t3]
ind3 = [idx for idx in ind3 if idx not in ind2]
ind3 = [idx for idx in ind3 if idx not in ind1]


ind4 = [index for index,value in enumerate(t) if value<=t4]
ind4 = [idx for idx in ind4 if idx not in ind3]
ind4 = [idx for idx in ind4 if idx not in ind2]
ind4 = [idx for idx in ind4 if idx not in ind1]

ind5 = [index for index,value in enumerate(t) if value<=t5]
ind5 = [idx for idx in ind5 if idx not in ind4]
ind5 = [idx for idx in ind5 if idx not in ind3]
ind5 = [idx for idx in ind5 if idx not in ind2]
ind5 = [idx for idx in ind5 if idx not in ind1]

ind6 = [index for index,value in enumerate(t) if value<=t6]
ind6 = [idx for idx in ind6 if idx not in ind5]
ind6 = [idx for idx in ind6 if idx not in ind4]
ind6 = [idx for idx in ind6 if idx not in ind3]
ind6 = [idx for idx in ind6 if idx not in ind2]
ind6 = [idx for idx in ind6 if idx not in ind1]

ind7 = [index for index,value in enumerate(t) if value<=T]
ind7 = [idx for idx in ind7 if idx not in ind6]
ind7 = [idx for idx in ind7 if idx not in ind5]
ind7 = [idx for idx in ind7 if idx not in ind4]
ind7 = [idx for idx in ind7 if idx not in ind3]
ind7 = [idx for idx in ind7 if idx not in ind2]
ind7 = [idx for idx in ind7 if idx not in ind1]



q1=(a1/6)*t**3+b1*t**2/2+c1*t+d1
q2=(a2/6)*t**3+b2*t**2/2+c2*t+d2
q3=(a3/6)*t**3+b3*t**2/2+c3*t+d3
q4=(a4/6)*t**3+b4*t**2/2+c4*t+d4
q5=(a5/6)*t**3+b5*t**2/2+c5*t+d5
q6=(a6/6)*t**3+b6*t**2/2+c6*t+d6
q7=(a7/6)*t**3+b7*t**2/2+c7*t+d7

q=np.concatenate((q1[ind1],q2[ind2],q3[ind3],q4[ind4],q5[ind5],q6[ind6],q7[ind7]))

v1=a1*t**2/2+b1*t+c1
v2=a2*t**2/2+b2*t+c2
v3=a3*t**2/2+b3*t+c3
v4=a4*t**2/2+b4*t+c4
v5=a5*t**2/2+b5*t+c5
v6=a6*t**2/2+b6*t+c6
v7=a7*t**2/2+b7*t+c7

v=np.concatenate((v1[ind1],v2[ind2],v3[ind3],v4[ind4],v5[ind5],v6[ind6],v7[ind7]))

acc1=a1*t+b1
acc2=a2*t+b2
acc3=a3*t+b3
acc4=a4*t+b4
acc5=a5*t+b5
acc6=a6*t+b6
acc7=a7*t+b7

acc=np.concatenate((acc1[ind1],acc2[ind2],acc3[ind3],acc4[ind4],acc5[ind5],acc6[ind6],acc7[ind7]))

j1=a1*np.ones((1,len(t))).T
j2=a2*np.ones((1,len(t))).T
j3=a3*np.ones((1,len(t))).T
j4=a4*np.ones((1,len(t))).T
j5=a5*np.ones((1,len(t))).T
j6=a6*np.ones((1,len(t))).T
j7=a7*np.ones((1,len(t))).T

j=np.concatenate((j1[ind1],j2[ind2],j3[ind3],j4[ind4],j5[ind5],j6[ind6],j7[ind7]))


t_final=time.time()

# print("Total time of the program:",t_final-t_inicial)


fig, axs = plt.subplots(4)

fig.suptitle('S-curve trajectory')
fig.tight_layout()
axs[0].plot(t, q,'r')
axs[0].set(ylabel='q(t) - position')
axs[1].plot(t, v,'g')
axs[1].set(ylabel='qdot - velocity')
axs[2].plot(t, acc,'b')
axs[2].set(ylabel='q2dot - aceleration')
axs[3].plot(t, j,'black')
axs[3].set(ylabel='q3dot - Jerk')

plt.xlabel('time')
plt.show()