#include <stdio.h> 


int main(){

    int p;                                                       // Tam sayı değişkeni tanımlama
    p = 77;                                                      // argüman atama
    int s = 777;                                                 // Tam sayı değişkeni tanımlama ve argüman atama
                   
    int level = 5;               
    float xp = 5.495;                                            // Ondalıklı sayı, 4 byte boyutu, 6-7 basamaklı sayılar
    double xps = 5.43248042348784234;                            // ondalıklı sayı, 8 byte boyutu, 15-16 basamaklı sayılar
    char server = 'H';                                           // Tek karakterler için char kullanılır ve tek karakterler ' ile yazılır
    char username[] = "Rorekain";                                // C dilinde nesne tabanlı olmadığı için string karakter türü yok. karakter dizisi oluşturuyoruz
     

    printf("Merhaba %s \n", username);                           // %s String ifadeyi yani karakter dizisini metinde  kullanmak için
    printf("Leveliniz: %d \n", level);                           // %d decimal demek sayı karakterleri için cümle içine bunu yazar ve sonunda değişkeni veririz.
    printf("Xp Düzeyiniz %%%f ve %%%lf \n", xp, xps);            // %f float ifade. %%f şeklinde yazınca '%f' değer olarak algılıyor bu yüzden iki adet %.   %lf double
    printf("%c Sunucusunda Oynuyorsun\n", server);               // %c char karakteri metinde kullanmak için 
    printf("%0.14f \n",xp);                                      // 0 dan sonra 14 basamak göster dedik. float olduğu için 6-7 basamak sonrasını yanlış hesaplar
    printf("%0.14lf",xp);                                        // double ile yap dediğimizden doğru hesaplayacak
    
    
    
    return 0;

}