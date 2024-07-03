#include <stdio.h>
#include <math.h> 

int main(){
    
    double x = sqrt(25);                       // karekök alma
    double y = pow(3,3);                       // üs alma
    double z = round(5.75);                    // yuvarlama
    double a = ceil(4.05);                     // bir üste yuvarlama
    double b = floor(7.88);                    // Tabana yuvarlama
    double c = fabs(-34234);                   // Mutlak değer alma
    double d = log(7);                         // logaritmasını alma
    double e = sin(45);                        // sin alma
    double f = cos(45);                        // cos alma
    double g = tan(45);                        // tan alma


    printf("\v%lf\v%lf\v%lf\v%lf\v%lf\v%lf\v%lf", x,y,z,a,b,c,d,e,f,g);



    return 0;
}