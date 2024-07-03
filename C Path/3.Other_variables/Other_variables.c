#include <stdio.h> 
#include <stdbool.h>                                        // bool kütüphanesi



int main(){

    bool r = true;                                            // 1 bytes (true or false)  çağırım: %d
    char y = 170;      // char x= 'x';                        // 1 bytes [-128 <--> +127] çağırım: tek harfli string karaktese %c, sayı varsa %d , sayı varsa karakter skalasındaki karşılığı için %c. FAZLA GİRİLİNCE BAŞA DÖNER -127 ye. %c verilecek olan input
    char cy[] = "Poyraz";                                     // 1 bytes Çağırım: %s. char tek karakter alabildiğinden string ifade belirtme şeklimiz budur      
    unsigned char uc = 254;                                   // 1 bytes [0 <--> 255] negatif yok.  Çağırım: tek harfli string karaktese %c, sayı varsa %d
    short s = 32000;                                          // 2 bytes [-32,768 <--> +32,767]  daha az yer kaplar. Çağırım %d
    unsigned short as = 65535;                                // 2 bytes [0 <--> 65,535] Çağırım: %d
    int i = 2140140140;                                       // 4 bytes [-2,147,483,648 <--> +2,147,483,648]  Çağırım: %d
    unsigned int ui = 4294294294;                             // 4bytes  [0 <--> 4,294,483,648]  Çağırım: %u
    long long int lli = 91234123412345123;                    // 8bytes  [-9 quintillion <--> +9 quintillion] Çağırım %lld
    unsigned  long long int ulli = 1881234123413435123;       // 8bytes  [0 <--> +18 quintillion] Çağırım %llu
   
   
   
    printf("%d\n",r);                                         // 1 or 0 döndürecek
    printf("%c\n",y);                                         // skaladakini döndürecek
    printf("%c\n",uc);                                        // skaladakini döndürecek
    printf("%d\n",i);                                         // argümanı döndürecek
    printf("%lld\n",lli);                                     // argümanı döndürecek

    return 0;
}