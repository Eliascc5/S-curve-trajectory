#include<stdio.h>
#include<math.h>
#include<stdlib.h>


#define MIN(a,b) (((a)<(b))?(a):(b))
#define MAX(a,b) (((a)>(b))?(a):(b))

float jmax = 1;
float jmin;

float vmax = 0.4;
float vi = 0;
float vf = 0.4;
float amax = 4; 
float amin;
 
 float T,Ta,Td,Tv,Tj1,Tj2,Tj,delta;

float qi = 0;
float qf = 3;

float q,qd,qdd,qddd;


float alima;
float alimd;
float vlim; // = vf-(Td-Tj2)*alimd;




void get_Straj(float t){

    //#Acceleration phase

    if (t>=0 & t<=Tj1){               //a) [0,Tj1]
        
        q = qi+vi*t+jmax*pow(t,3)/6;
        qd = vi+jmax*pow(t,2)/2;
        qdd = jmax*t;
        qddd = jmax;

    } else if (t>Tj1 & t<=Ta-Tj1){   //b) [Tj1,Ta-Tj1]

        q = qi+vi*t+(alima/6)*(3*pow(t,2)-3*Tj1*t+pow(Tj1,2));
        qd = vi+amax*(t-Tj1/2);
        qdd = jmax*Tj1;
        qddd = 0;

    } else if (t>Ta-Tj1 & t<=Ta){    //c) [Ta-Tj1,Ta]
        
        q = qi+(vlim+vi)*Ta/2-vlim*(Ta-t)-jmin*pow(Ta-t,3)/6;
        qd = vmax+jmin*pow(Ta-t,2)/2;
        qdd = -jmin*(Ta-t);
        qddd = jmin;

    }

    /*-------------Constant phase ----------------*/
    else if (t>Ta & t<=Ta+Tv){

        q = qi+(vlim+vi)*Ta/2+vlim*(t-Ta);
        qd = vmax;
        qdd = 0;
        qddd = 0;

    }
    /*-------------Dese phase ----------------*/

    else if (t>=T-Td & t<=T-Td+Tj2){
        q=qf-(vlim+vf)*Td/2+vlim*(t-T+Td)-jmax*(pow(t-T+Td,3)/6);
        qd=vlim-jmax*(pow(t-T+Td,2)/2);
        qdd=-jmax*(t-T+Td);
        qddd=jmin;

    } else if (t>T-Td+Tj2 & t<=T-Tj2){
        q=qf-(vlim+vf)*Td/2+vlim*(t-T+Td)+(alimd/6)*(3*pow(t-T+Td,2)-3*Tj2*(t-T+Td)+pow(Tj2,2));
        qd=vlim+alimd*(t-T+Td-Tj2/2);
        qdd = -jmax*Tj2;
        qddd = 0;


    } else if (t>T-Tj2 & t<=T){

        q = qf-vf*(T-t)-jmax*(pow(T-t,3)/6);
        qd = vf+jmax*(pow(T-t,2))/2;
        qdd = -jmax*(T-t);
        qddd = jmax;

    }

    printf("Este es el final\n");

}


void update_ScurveTraj(float qf ,float qi, float vi,float vf ,float vmax,float amax,float jmax){

jmin = -jmax;
amin = -amax;

if (qf < 0){
       
    amax = -amax;
    vmax = -vmax;
    jmax = -jmax;
}
    
volatile float Tjaux = MIN(sqrt(fabs(vf-vi)/jmax),amax/jmax);


if (Tjaux<amax/jmax){
    if (qf-qi > Tjaux*(vi+vf)) {printf("the trajectory is feasible \n");}    
    else {printf("the trajectory is NOT \n");}      
}        
else if (Tjaux == amax/jmax){
    if (qf-qi > 0.5*(vi+vf)*(Tjaux+abs(vi+vf)/amax)) {printf("the trajectory is feasible\n");}       
    else {printf("the trajectory is NOT feasible\n");}      
}
//Phase 1: acceleration
if ((vmax-vi)*jmax < pow(amax,2)){
    printf("amax is NOT reached\n");
    
    Tj1=sqrt(fabs(vmax-vi)/jmax);
    Ta=Tj1*2;
}
else{
    printf("amax is reached\n");
    Tj1=amax/jmax;
    Ta=Tj1+(vmax-vi)/amax;
}
    
//Phase 3: Desacceleration


if ((vmax-vf)*jmax < pow(amax,2)){
    printf("amin is NOT reached\n");
    
    Tj2=sqrt(fabs(vmax-vf)/jmax);
    Td=Tj2*2;
}
else{
    printf("amin is reached\n");
    Tj2=amax/jmax;
    Td=Tj2+(vmax-vf)/amax;
}


Tv = (qf-qi)/vmax - Ta/2*(1+vi/vmax)-Td/2*(1+vf/vmax);

if (Tv>0){
    printf("the max velocity is reached\n");
}
else{
    printf("CASE 2\n");
    printf("In this case vmax is NOT reached, so Tv=0\n");
    Tj1=amax/jmax;
    Tj2=Tj1;
    Tj=Tj1;
    delta = (pow(amax,4)/pow(jmax,2))+2*(pow(vi,2)+pow(vf,2))+amax*(4*(qf-qi)-2*(amax/jmax)*(vi+vf));
    Ta=((pow(amax,2)/jmax)-2*vi+sqrt(delta))/(2*amax);
    Td=((pow(amax,2)/jmax)-2*vf+sqrt(delta))/(2*amax);
    Tv=0;
    //int i=0;
    
    if (Ta<2*Tj || Td<2*Tj){
        printf("entre\n");
        while (!(Ta>2*Tj & Td>2*Tj)){
            
            amax=amax*0.99;
            Tj=amax/jmax;
            delta = (pow(amax,4)/pow(jmax,2))+2*(pow(vi,2)+pow(vf,2))+amax*(4*(qf-qi)-2*(amax/jmax)*(vi+vf));
            Ta=((pow(amax,2)/jmax)-2*vi+sqrt(delta))/(2*amax);
            Td=((pow(amax,2)/jmax)-2*vf+sqrt(delta))/(2*amax);
            
            //print(f'{i}',amax)
            //i++;
 
            if (Ta<0){
                Ta=0;
                Tj1=0;
                Td=2*((qf-qi)/(vf+vi));
                Tj2=(jmax*(qf-qi)-sqrt(jmax*(jmax*(pow(qf-qi,2))+pow(vf+vi,2)*(vf-vi))))/(jmax*(vf+vi));
                break;
            }
            if (Td<0){
                printf("acaaaaa\n");
                Td=0;
                Ta=2*((qf-qi)/(vf+vi));
                Tj1=(jmax*(qf-qi)-sqrt(jmax*(jmax*(pow(qf-qi,2))-pow(vf+vi,2)*(vf-vi))))/(jmax*(vf+vi));
                Tj2=0;
                break;
            }
        }
    }

}

}

int main (void){

update_ScurveTraj(qf,qi, vi,vf,vmax,amax, jmax);

alima=jmax*Tj1;
alimd=-jmax*Tj2;
vlim = vi+(Ta-Tj1)*alima; 

T=Ta+Td+Tv;

printf("Ta: %f\n",Ta);
printf("Tj1: %f\n",Tj1);
printf("Tj2: %f\n",Tj2);
printf("Tv: %f\n",Tv);
printf("Td: %f\n",Td);
printf("T: %f\n",T);

get_Straj(5.668080);

printf("q,qd,qdd:  %f,%f,%f",q,qd,qdd);

    return 0;
}