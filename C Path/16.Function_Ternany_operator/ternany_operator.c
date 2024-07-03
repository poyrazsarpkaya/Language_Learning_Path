#include <stdio.h>

int big(int a, int b){

    return (a>b) ? a : b;                                // Böyle ikili durumlarda if else ile uğraşmaktansa ternany operator kullanmak daha mantıklı

}


int main (){

    int x;
    int y;

    printf("\rDeger giriniz: ");
    scanf("%d", &x);
    printf("\rDeger giriniz: ");
    scanf("%d", &y);

    int max = big(x,y);
   
    printf("\r%d Sayısı Daha Büyüktür.",max);


    return 0;
}