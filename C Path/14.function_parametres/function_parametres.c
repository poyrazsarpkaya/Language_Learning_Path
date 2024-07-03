#include <stdio.h>


void car(char brand[], char model[] ){                          // Fonksiyonlarda girdinin türünü de yazmamız gerekir

    printf("\r Welcome to %s %s ", brand,model);
}


int main (){
     
     char b[15];
     char m[15];

     printf("\rBrand? ");
     scanf("%s",&b);
     
     printf("\rModel? ");
     scanf("%s",&m );

     car(b,m);


     return 0;
}