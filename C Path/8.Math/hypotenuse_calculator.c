#include <stdio.h>
#include <math.h>


int main (){
     
    double x;
    double y;
    double z;

    printf("\rx kenarını giriniz: ");
    scanf("%lf", &x);
    
    printf("\ry kenarını giriniz: ");
    scanf("%lf", &y);

    z = sqrt(pow(x,2) + pow(y,2));

    printf("\rc kenarının uzunluğu: %lf", z);
     
    return 0;
}