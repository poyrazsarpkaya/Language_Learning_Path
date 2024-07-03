#include <stdio.h>
#include <string.h>


void control(char c_name[15]){                                     
    if (strlen(c_name) == 0){
        printf("Your name cannot be empty\n");
        return namme();                                       // 4. Değer uzunluğu yoksa input alma fonksiyonu döndürüldü
    }
    else{
        printf("Hello Mr.%s.How does your day go?", c_name);
    }


}


void namme(){

    char name[15]; 

    printf("Enter your name: ");
    fgets(name,15,stdin);                                     // 2.İnput alındı ve gerekli düzenleme yapıldı.
    name[strlen(name)-1] = '\0';

    control(name);                                            // 3.Kontrole yollandı.
}



int main (){

    namme();                                                  // 1.Fonksiyonu çalıştırıldı.
    
    return 0;
}