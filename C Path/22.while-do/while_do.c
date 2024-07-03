#include <stdio.h>
#include <string.h>



int main (){

    char name[15]; 
    int length;                                           // kullanılacak olan değişecek olanlar do while dışında olmalı
    
    do                                                    // do while döngüsü, önce çalıştırır sonra kontrol eder.
    {
       
       printf("Enter your name: ");
       fgets(name,15,stdin);
       name[strlen(name)-1] = '\0';                      
       length = name[strlen(name)];
   
    } while (length<=0);                                  // HEP SIFIR GÖRÜYOR SIKINTI VAR
    
      printf("\nWelcome %s", name);
   
   
                                                            
    return 0;
}