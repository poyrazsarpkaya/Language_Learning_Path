#include <stdio.h>
#include <math.h>

double re(double a){                          // eger ki return kullanacaksan geri dondurulucek olan degerin türünde fonksiyon belirleyeceksin
                                              // bu yüzden main fonksiyonda int kullanılıyor 0 dondurdugu icin ;)
     double result = pow(a,2);
     return result;                           


}

int main (){

    double x = re(4.5); 
    printf("\r%f",x);                        // test icin printf

    return 0;
}