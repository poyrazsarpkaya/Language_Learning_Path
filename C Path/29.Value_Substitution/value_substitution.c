#include <stdio.h>
#include <string.h>

int main (){

   /*
    char x = 'X';
    char y = 'Y';

    char temp;                           // değerlerin yer değiştirmesi için 3. bir değişkene ihtiyacımız var. Tek tek atayarak değişiyor.

    temp = x;                            // char değişkenlerinde değer değişimi
    x = y;
    y = temp;

    printf("%c\n%c", x,y);               // Özel durum oluştuğundan c ile çağırdık


   */

   char brand[10] = "BMW";
   char model[10] = "M8";

   char temp[10];

   strcpy(temp,brand);                  // string ifadelerde değerler string kütüphanesi ile değiştirilebiliyor.
   strcpy(brand,model);
   strcpy(model,temp);

   printf("%s\n%s", brand,model);





    return 0;
}

