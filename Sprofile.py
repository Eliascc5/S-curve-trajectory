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

jmax = 2

vmax = 0.4

amax = 4


qf = math.sqrt(3)

if qf <= 0.5:
    vmax=vmax/4


aux = math.sqrt((vmax*jmax))
   
if aux <= amax: 
    # print("i'm in")
    amax = aux

if (qf < 0):
       
    amax = -amax
    vmax = -vmax
    jmax = -jmax
    

    
T = (amax/jmax)+(vmax/amax)+(qf/vmax)

print(T)

if  amax/jmax + vmax/amax < T/2:
    t1= amax/jmax
    t3 = t1 + vmax/amax
else:
    print("Error en paramatros!")
    sys.exit()

t2=t3-t1
t4=T-t3
t5=T-t2
t6=T-t1

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

print("Total time of the program:",t_final-t_inicial)


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