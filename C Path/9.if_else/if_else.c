#include <stdio.h>
#include <math.h>


int main (){

    short age;
    age >0;
    
    printf("\rLutfen yasinizi giriniz: ");
    scanf("%d", &age);

    if(age>=18){                                                     // && = and    || = or   !age = Not operatörü

        printf("\rKayit basarili ");

    }

    else if(age<0){

        printf("\rÖnce doğman gerekiyor.. ve tabi büyümen");

    }
    
    else{
        printf("\rkayit basarisiz");
    }


    return 0;
}