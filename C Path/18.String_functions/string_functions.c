#include <stdio.h>
#include <string.h>


int main (){

    char str1[] = "Poyraz";
    char str2[] = "Sarpkaya";

    //strlwr(str1);                                          // karakterleri küçültür
    //strupr(str2);                                          // karakterleri Büyültür
    //strcat(str1, str2);                                    // sondakini ilkine ekler
    //strncat(str1, str2, 4);                                // sondakini ilkine ekler belirtilen(n) karakter saysısı kadar
    //strcpy(str1, str2);                                    // sondakini ilkine kopyalıyor
    //strncpy(str1, str2, 3);                                // sondakini ilkine belirtilen(n) karakter saysısı kadar olan kısmını kopyalıyor. gerisi aynı kalıyor
    
    //strset(str1, '!');                                     // tüm karakterleri ünlem yap
    //strnset(str1, '!',5);                                  // tüm karakterleri belirtilen(n) karakter saysısı kadar olan kısmını ünlem yapıyor. gerisi aynı kalıyor
    //strrev(str1);                                          // stringi ters çevir
    

    //int result = strlen(str1);                             // verilen stringin uzunluğunu alır.


    //printf("%s", str1);       


     
    // int result = strcmp(str1,str2);                          // stringler arası karşılaştırma yapar. aynı mı diye. Aynı ise 0 döndürür.
    // int result = strncmp(str1,str2,2);                       // stringler arası elirtilen(n) karakter saysısı kadar olan kısmını karşılaştırma yapar. aynı mı diye. Aynı ise 0 döndürür.
    // int result = strcmpi(str1,str2);                         // stringler arası karşılaştırma yapar. aynı mı diye. Aynı ise 0 döndürür. (BÜYÜK küçük Fark Etmez)
    // int result = strnİcmp(str1,str2,2);                      // stringler arası elirtilen(n) karakter saysısı kadar olan kısmını karşılaştırma yapar. aynı mı diye. Aynı ise 0 döndürür. (BÜYÜK küçük Fark Etmez)



    if(result==0){

        printf("Girilen degerler Aynılar");
    }
    else{
        printf("Girilen degerler Aynı Değil");
    }



    return 0;
}