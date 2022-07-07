#include <stdio.h>
#include<stdlib.h>
#include <math.h>

//Jerk = 2*(amax**2/vmax)

//Variables globales

float time[5] , T; 

#define nbCoeff 4 
#define segments 7


float coeff[nbCoeff][segments];

float q, qdot,q2dot,q3dot;

void update_ScurveTraj(float qf ,float vmax,float amax,float jmax){

if (qf <= 0.5){  //Prenguntar cuando la distancia es muy chica
    vmax=vmax/4;
};

volatile float aux = sqrt((vmax*jmax));

if (aux <= amax){
    amax = aux;
} ;


if (qf < 0){
    amax = -amax;
    vmax = -vmax;
    jmax = -jmax;

};


T = (amax/jmax)+(vmax/amax)+(qf/vmax);


if  (amax/jmax + vmax/amax < T/2){
    time[0]= amax/jmax;
    time[2] = time[0] + vmax/amax;

}else{
    printf("Error en paramatros!\n");
    exit(EXIT_FAILURE);
};

// printf("El valor de amax es: %f \n",amax);
// printf("El valor de vmax es: %f \n",vmax);
// printf("El valor de jmax es: %f \n",jmax);
// printf("El valor de T max es: %f \n",T);

time[1]=time[2]-time[0];
time[3]=T-time[2];
time[4]=T-time[1];
time[5]=T-time[0];

printf("El valor de time[0]  es: %f \n",time[0]);
// printf("El valor de time[2]  es: %f \n",time[2]);
// printf("El valor de time[3]  es: %f \n",time[3]);

//coeffs "a"
coeff[0][0]=coeff[0][6]=jmax;             //a1=a7 = jmax
coeff[0][1]=coeff[0][3]=coeff[0][5]=0;    //a2=a4 = 0
coeff[0][2]=coeff[0][4]=-jmax;            //a3=a5 = -jmax

//coeffs "b"
coeff[1][0]=0;
coeff[1][1]=amax;
coeff[1][2]=amax+jmax*time[1];
coeff[1][3]=0;
coeff[1][4]=jmax*time[3];
coeff[1][5]=-amax;
coeff[1][6]=-amax-jmax*time[5];

//coeffs "c"
coeff[2][0]=0;
for (int i=1; i<segments;i++){
    coeff[2][i]=((coeff[0][i-1]*pow(time[0],2))/2+coeff[1][i-1]*time[0]+coeff[2][i-1])-((coeff[0][i]*pow(time[0],2))/2+coeff[1][i]*time[0]);
}

//coeffs "d"
coeff[3][0]=0;
for (int i=1; i<segments;i++){
    coeff[3][i]=((coeff[0][i-1]*pow(time[0],3))/6+(coeff[1][i-1]*pow(time[0],2))/2+coeff[2][i-1]*time[0]+coeff[3][i-1])-((coeff[0][i]*pow(time[0],3))/6+(coeff[1][i]*pow(time[0],2))/2+coeff[2][i]*time[0]);
}

// printf("c1,c2,c3 %f,%f,%f\n",coeff[2][0],coeff[2][1],coeff[2][2]);


}


void get_Straj(float t){

    if (t>=0 & t<=time[0]){
        // printf("Estoy en el segmento 1 \n");
        q=(coeff[0][0]/6)*pow(t,3)+coeff[1][0]*pow(t,2)/2+coeff[2][0]*t+coeff[3][0]; //pos
        qdot=coeff[0][0]*pow(t,2)/2+coeff[1][0]*t+coeff[2][0]; //speed
        q2dot=coeff[0][0]*t+coeff[1][0]; //accel
        // q3dot=coeff[0][0]; Jerk


    }else if (t>time[0] & t<=time[1]){
        // printf("Estoy en el segmento 2 \n");
        q=(coeff[0][1]/6)*pow(t,3)+coeff[1][1]*pow(t,2)/2+coeff[2][1]*t+coeff[3][1]; //pos
        qdot=coeff[0][1]*pow(t,2)/2+coeff[1][1]*t+coeff[2][1]; //speed
        q2dot=coeff[0][1]*t+coeff[1][1]; //accel
        // q3dot=coeff[0][1]; Jerk


    }else if (t>time[1] & t<=time[2]){
        // printf("Estoy en el segmento 3 \n");
        q=(coeff[0][2]/6)*pow(t,3)+coeff[1][2]*pow(t,2)/2+coeff[2][2]*t+coeff[3][2]; //pos
        qdot=coeff[0][2]*pow(t,2)/2+coeff[1][2]*t+coeff[2][2]; //speed
        q2dot=coeff[0][2]*t+coeff[1][2]; //accel
        // q3dot=coeff[0][2]; Jerk

    }else if (t>time[2] & t<=time[3]){
        // printf("Estoy en el segmento 4 \n");
        q=(coeff[0][3]/6)*pow(t,3)+coeff[1][3]*pow(t,2)/2+coeff[2][3]*t+coeff[3][3]; //pos
        qdot=coeff[0][3]*pow(t,2)/2+coeff[1][3]*t+coeff[2][3]; //speed
        q2dot=coeff[0][3]*t+coeff[1][3]; //accel
        // q3dot=coeff[0][3]; Jerk


        // printf("El valor de velocidad es: %f",qdot);
    }else if (t>time[3] & t<=time[4]){
        // printf("Estoy en el segmento 5 \n");
        q=(coeff[0][4]/6)*pow(t,3)+coeff[1][4]*pow(t,2)/2+coeff[2][4]*t+coeff[3][4]; //pos
        qdot=coeff[0][4]*pow(t,2)/2+coeff[1][4]*t+coeff[2][4]; //speed
        q2dot=coeff[0][4]*t+coeff[1][4]; //accel
        // q3dot=coeff[0][4]; Jerk

        // printf("El valor de velocidad es: %f",qdot);


    }else if (t>time[4] & t<=time[5]){
        // printf("Estoy en el segmento 6 \n");
        q=(coeff[0][5]/6)*pow(t,3)+coeff[1][5]*pow(t,2)/2+coeff[2][5]*t+coeff[3][7]; //pos
        qdot=coeff[0][5]*pow(t,2)/2+coeff[1][5]*t+coeff[2][5];  //speed
        q2dot=coeff[0][5]*t+coeff[1][5]; //accel
        // q3dot=coeff[0][5]; Jerk
    }
    else if (t>time[5] & t<=time[5]){
        // printf("Estoy en el segmento 7 \n");
        q=(coeff[0][6]/6)*pow(t,3)+coeff[1][6]*pow(t,2)/2+coeff[2][6]*t+coeff[3][6]; //pos
        qdot=coeff[0][6]*pow(t,2)/2+coeff[1][6]*t+coeff[2][6]; //speed
        q2dot=coeff[0][6]*t+coeff[1][6]; //acel
        // q3dot=coeff[0][6]; Jerk

    }else{
        printf("Error t no esta dentro del rango\n");
        exit(EXIT_FAILURE); 
        
    }

}

int main (void){


float jmax = 1;
float vmax = 0.4;
float amax= 4;
float qf = sqrt(3);  //distance

// printf("distance : %f\n",qf);

float t = 4.34; 


update_ScurveTraj(qf,vmax,amax,jmax);
get_Straj(t);

    return 0;
}

