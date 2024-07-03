#include <stdio.h>
#include <string.h>



int main (){

    char name[15]; 

    printf("Enter your name: ");
    fgets(name,15,stdin);                                    
    name[strlen(name)-1] = '\0';
 
    while (strlen(name) == 0 ){                                      // while döngüsü, Koşul kontrol edilir doğru ise kodlar çalıştırılır.
        printf("Your name cannot be empty\n");                       // Name değişkenine kullanıcı tarafından verilen argüman uzunluğu 0 ise yani yoksa sürekli ismi iste
        printf("Enter your Name: ");
        fgets(name,15,stdin);
        name[strlen(name)-1] = '\0';
    }


    return 0;
}