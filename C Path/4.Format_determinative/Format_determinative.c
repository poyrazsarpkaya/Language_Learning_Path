#include <stdio.h>


int main(){

    float  product1 = 15.70;
    float  product2 = 15.80;
    float  product3 = 15.90;
     

    printf("Product1: %0.2f Tl\n", product1);                              // sıfırdan sonra kaç basamak göstermek istiyorsan 
    printf("Product2: %10.2f Tl\n", product2);                             // öncesine kaç boşluk
    printf("Product3: %-10.2f Tl\n", product3);                            // sonrasına kaç boşluk


    return 0;
}