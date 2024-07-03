#include <stdio.h>
#include <math.h>


int main (){
    
    const float pi = 3.18;
    float radius;
    float circumference;
    float area;

    printf("Enter the radius of the circle:  ");
    scanf("%f", &radius);

    circumference = 2 * pi * radius;
    area = pi * pow(radius,2);

    printf("Area: %f\nCircumference: %f\n ", area, circumference);

    return 0;
}