#include <stdio.h>
#include <string.h>

int main (){

    char pc_model[][10] = {"MSI","Lenovo","Imac"};                    // ilk köşeli parantez tek karakter olmadıklarını söylüyor. ikincisi karakterlerin sınırını
    strcpy(pc_model[0], "CS:GO");                                     // Değiştirmek için kütüphane kullanmalıyız direkt char ile olmuyor.


    printf("%s\n", pc_model[0]);

    
    for(int i= 0; i<sizeof(pc_model)/(sizeof(pc_model[0])); i+=1){
        printf("%s\n", pc_model[i]);

     }


    return 0;
}