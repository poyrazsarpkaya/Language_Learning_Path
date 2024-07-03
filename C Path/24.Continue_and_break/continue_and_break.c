#include <stdio.h>

int main (){

    for(int i =1; i<=15; i+=1){
          if(i==3 || i==5){                      
            continue;                                   // Durum sağlandığında onu işleme ve kod çalışmaya devam etsin
          }
          
          else if(i==14){                               // Durum sağlandığında bitir
            break;
          }

    printf("\n%d", i);

    }
       


    return 0;
}