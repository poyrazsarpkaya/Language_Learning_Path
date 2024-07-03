#include <stdio.h>
#include <ctype.h>                                                               // touper için çektik bu kütüphaneyi


int main (){

    char unit;
    float  temp; 
    
    printf("\rsicaklik birimini gir\nCelsius(C)\nFahrenheit(F)\n");
    scanf("%c", &unit);

    unit = toupper(unit);                                                         // Büyük harf istendiğinde küçük olanı da kapsa
    //unit = tolower(unit);                                                       // Küçük harf istendiğinde büyük olanı da kapsa
   
    printf("\rSicaklik degerini giriniz: ");
    scanf("%f", &temp);



    if(unit=='c'){
        temp = (temp *  9/5) +32; 
        printf("\rSicaklik: %.2f Fahrenheit", temp);    
    }
    
    else if(unit =='f'){
        temp = (temp * 9/5) +32;
        printf("\rSicaklik: %.2f Celcius", temp);

    }
        
    else{
        printf("\rGecerli bir deger giriniz");
    }




    return 0;
}