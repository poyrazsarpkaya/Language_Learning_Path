#include <stdio.h>
#include <math.h>


int main (){

    char lecture_note;

    printf("\rNotunuzu giriniz: ");
    scanf("%c", &lecture_note);


    switch (lecture_note) 
    {
    case 'A':
        printf("\rEFSANEVİ!");
        break;
    case 'B':
        printf("\rMükemmel");
    case 'C':
        printf("\rGüzel");

    default:
        printf("\rGecerli bir not gir ");
        break;
    }




    return 0;
}