#include <stdio.h>


void sort(int array[], int size){                  
    
    for(int i = 0; i <size-1; i++){                    // 9 elemana ve 8 dizi karakterine sahip bu dizimizin 
                                                       // son diziden sonra +1 alınıp büyük küçük kontrolü yapılamayacağı için -1 verdik
        for(int j= 0; j<size-1; j++){                  // Her diziyi 7. dizine kadar kontrol ettirdik. sağa ata ata kontrol ettik.

            if(array[j] > array[j+1]){                 // 7. diziye geldiğimiz  +1 yani 8. dizi de kontrol edilmiş oldu.

                int temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;

            }
        }

    }
}


void print_sort_array(int array[] , int size){

    for(int i = 0; i<size; i+=1){ 
        printf("%d\t", array[i]);


    }

    
}



int main(){


    int range[] = {10,90,30,40,20,70,80,60,50};
    int size = sizeof(range)/sizeof(range[0]);            // kaç dizi kontrol edip sıralayacağımızı bilmek için kaç TANE olduklarını öğrendik.

    sort(range,size);
    print_sort_array(range,size);


    return 0;
}