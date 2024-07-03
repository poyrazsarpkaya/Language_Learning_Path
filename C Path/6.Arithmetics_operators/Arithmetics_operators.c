#include <stdio.h>


int main(){

     /*
     Toplama '+'
     Çıkarma '-'
     Çarpma  '*'
     Bölme   '/'
     Mod alma '%'
     Arttırma '++'
     Azaltma  '--'
     */


    int x = 56;
    int y = 44;
    int z = x-y;
    float t = x / (float) y;                  // işlem değişkenini ve işlemdeki en aza bir değerin float olması gerekiyor
    int m = x % y;                            
    x--;
    x++;
    x++;
    
    x = x+2;
    x+=2;
    x=x*4;
    x*=4;
    x%=2;
    x = x%2;


    printf("%d\n", x+y);
    printf("%d\n",z);
    printf("%f\n",t);
    printf("%d\n",m);
    printf("%d",x);

    return 0;
}