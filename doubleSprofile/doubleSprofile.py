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


t_inicial=time.time()
sns.set_theme()

jmax = 1
jmin = -jmax

vmax = 1  #m/s
vmin = -vmax
vi = 0
vf = 0 
amax = 4
amin = -amax 

qi=  5
qf = -0.001  #m

inv= False

if (qf < qi):
    
    inv = True
    
    print("Inversion de valores!")
    
    qi = -qi
    qf = -qf
    vi = -vi
    vf = -vf
    
    vmax = -vmin
    vmin = -vmax
    amax = -amin 
    amin = -amax
    jmax = -jmin
    jmin = -jmax

Tjaux= min(math.sqrt(abs(vf-vi)/jmax),amax/jmax)


if Tjaux < amax/jmax:
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
if (vmax-vi)*jmax < pow(amax,2):
    print("amax is NOT reached")
    
    Tj1=math.sqrt(abs(vmax-vi)/jmax)
    Ta=Tj1*2
else:
    print("amax is reached")
    Tj1=amax/jmax
    Ta=Tj1+(vmax-vi)/amax
    
#Phase 3: Desacceleration

if (vmax-vf)*jmax < pow(amax,2):
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
            Tj1=Tj
            Tj2=Tj
            delta = (pow(amax,4)/pow(jmax,2))+2*(pow(vi,2)+pow(vf,2))+amax*(4*(qf-qi)-2*(amax/jmax)*(vi+vf))
            Ta=((pow(amax,2)/jmax)-2*vi+math.sqrt(delta))/(2*amax)
            Td=((pow(amax,2)/jmax)-2*vf+math.sqrt(delta))/(2*amax)
            
            # print(f'{i}',amax)
            i+=1
 
            if Ta<0:
                Ta=0
                Tj1=0
                Td=2*((qf-qi)/(vf+vi))
                Tj2=(jmax*(qf-qi)-math.sqrt(jmax*(jmax*(pow(qf-qi,2))+pow(vf+vi,2)*(vf-vi))))/(jmax*(vf+vi))
                break
            if Td<0:
                #print("acaaaaa")
                Td=0
                Ta=2*((qf-qi)/(vf+vi))
                Tj1=(jmax*(qf-qi)-math.sqrt(jmax*(jmax*(pow(qf-qi,2))-pow(vf+vi,2)*(vf-vi))))/(jmax*(vf+vi))
                Tj2=0
                break
        

#%%

alima=jmax*Tj1
alimd=-jmax*Tj2
vlim=vi+(Ta-Tj1)*alima # = vf-(Td-Tj2)*alimd



print("amax:",amax)
print("Ta :",Ta)
print("Td :",Td)
print("Tv:",Tv)
print("Tj1:",Tj1)
print("Tj2:",Tj2)

T=Ta+Td+Tv




N=100
t=np.linspace(0,T,N)


ind1 = [index for index,value in enumerate(t) if value<=Tj1]

ind2 = [index for index,value in enumerate(t) if value<=Ta-Tj1]
ind2 = [idx for idx in ind2 if idx not in ind1]

ind3 = [index for index,value in enumerate(t) if value<=Ta]
ind3 = [idx for idx in ind3 if idx not in ind2]
ind3 = [idx for idx in ind3 if idx not in ind1]

ind4 = [index for index,value in enumerate(t) if value<=Ta+Tv]
ind4 = [idx for idx in ind4 if idx not in ind3]
ind4 = [idx for idx in ind4 if idx not in ind2]
ind4 = [idx for idx in ind4 if idx not in ind1]

ind5 = [index for index,value in enumerate(t) if value<=T-Td+Tj2]
ind5 = [idx for idx in ind5 if idx not in ind4]
ind5 = [idx for idx in ind5 if idx not in ind3]
ind5 = [idx for idx in ind5 if idx not in ind2]
ind5 = [idx for idx in ind5 if idx not in ind1]

ind6 = [index for index,value in enumerate(t) if value<=T-Tj2]
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


#Acceleration phase
#a) [0,Tj1]


q1=qi+vi*t+jmax*pow(t,3)/6
qd1=vi+jmax*pow(t,2)/2
qdd1=jmax*t
qddd1=jmax*np.ones((len(t)))

#b) [Tj1,Ta-Tj1]

q2=qi+vi*t+(alima/6)*(3*pow(t,2)-3*Tj1*t+pow(Tj1,2))
qd2=vi+alima*(t-Tj1/2)
qdd2=jmax*Tj1*np.ones((len(t)))
qddd2=0*np.ones((len(t)))

#c) [Ta-Tj1,Ta]

q3=qi+(vlim+vi)*Ta/2-vlim*(Ta-t)-jmin*pow(Ta-t,3)/6
qd3=vlim+jmin*pow(Ta-t,2)/2
qdd3=-jmin*(Ta-t)
qddd3=jmin*np.ones((len(t)))
###############################################
#Constant
q4=qi+(vlim+vi)*Ta/2+vlim*(t-Ta)
qd4=vlim*np.ones((len(t)))
qdd4=0*np.zeros((len(t)))
qddd4=0*np.ones((len(t)))

###############################################
#desa phase

q5=qf-(vlim+vf)*Td/2+vlim*(t-T+Td)-jmax*(pow(t-T+Td,3)/6)
qd5=vlim-jmax*(pow(t-T+Td,2)/2)
qdd5=-jmax*(t-T+Td)
qddd5=jmin*np.ones((len(t)))

q6=qf-(vlim+vf)*Td/2+vlim*(t-T+Td)+(alimd/6)*(3*pow(t-T+Td,2)-3*Tj2*(t-T+Td)+pow(Tj2,2))
qd6=vlim+alimd*(t-T+Td-Tj2/2)
qdd6=-jmax*Tj2*np.ones((len(t)))
qddd6=0*np.ones((len(t)))

q7=qf-vf*(T-t)-jmax*(pow(T-t,3)/6)
# print("Valores en tramo 7:", qf,vf,T,jmax)
qd7=vf+jmax*(pow(T-t,2))/2
qdd7=-jmax*(T-t)
qddd7=jmax*np.ones((len(t)))



q=np.concatenate((q1[ind1],q2[ind2],q3[ind3],q4[ind4],q5[ind5],q6[ind6],q7[ind7]))
qd=np.concatenate((qd1[ind1],qd2[ind2],qd3[ind3],qd4[ind4],qd5[ind5],qd6[ind6],qd7[ind7]))
qdd=np.concatenate((qdd1[ind1],qdd2[ind2],qdd3[ind3],qdd4[ind4],qdd5[ind5],qdd6[ind6],qdd7[ind7]))
qddd=np.concatenate((qddd1[ind1],qddd2[ind2],qddd3[ind3],qddd4[ind4],qddd5[ind5],qddd6[ind6],qddd7[ind7]))

if inv:
    q=-q
    qd=-qd
    qdd=-qdd
    qddd=-qddd

fig, axs = plt.subplots(4)

fig.suptitle('S-curve trajectory')
fig.tight_layout()
axs[0].plot(t, q,'r')
axs[0].set(ylabel='q(t) - position')
axs[1].plot(t, qd,'g')
axs[1].set(ylabel='qdot - velocity')
axs[2].plot(t, qdd,'b')
axs[2].set(ylabel='q2dot - aceleration')
axs[3].plot(t, qddd,'black')
axs[3].set(ylabel='q3dot - Jerk')

plt.xlabel('time')
plt.show()