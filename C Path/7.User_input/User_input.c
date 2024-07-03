#include <stdio.h>
#include <string.h>


int main(){
   

   char name[20];                                         // 20 karakter sınırı verdik
   int age;
   
   printf("What's your name?\n");
   // scanf("%s", &name);
   fgets(name,20,stdin);                                  // fgets boşluk bırakarak yazabildiğimiz bir komut scanf gibi diğerinputa değeri atmaz. Verilen değerden sonra boşluk bırakır!
   name[strlen(name)-1] = '\0';                           // kodun uzunluğunu alıp sondaki satır atlamayı silip null yani boşluk karakteri atıyoruz sonuna


   printf("How old are you?\n");
   scanf("%d",&age);                                       // Bu komut kullanıcıdan veri almamızı sağlar, alınan argümanın atanacak olan değişkenin başına & konur! girilen veriden sonra boşluk bırakıp yazarsak o da 2. inputa scanfe gidiyor

   printf("%s Adınız " , name);
   printf("%d ve yaşınız databaseye kayıt edildi\n",age);
   

   
   return 0;
}