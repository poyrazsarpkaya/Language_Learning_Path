#include <stdio.h>
#include <stdlib.h>


typedef struct{                                             // struct tanımlamanın başka bir yolu. Kısa değişkenler için kullanılabilir.

    char username[20];
    char password[20];
    int id;


}sign_in; 



int main(){

    
    sign_in account_1 = {"Crazy_boy", "qwerasd", 5345345};

    sign_in pointer = NULL;


    printf("\nYour Username: %s", account_1.username);


    return 0;
}