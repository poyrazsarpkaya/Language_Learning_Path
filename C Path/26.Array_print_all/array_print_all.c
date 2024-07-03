#include <stdio.h>

int main (){

    int top_10_lvl[] = {100,200,300,400,500,600,700,800,900,1000};

   // printf("%d\n" , sizeof(top_10_lvl));                                  // int değeri 4 bytettır, Listedekilerin boyutunu aldı
   
   for(int i = 0; i<sizeof(top_10_lvl)/sizeof(top_10_lvl[2]); i++){         // toplam boyutu bir değerin botuna böldürdük. Kaç adet olduğunu verdi. 40/0
    printf("%d\n", top_10_lvl[i]);
   }


    return 0;   
}