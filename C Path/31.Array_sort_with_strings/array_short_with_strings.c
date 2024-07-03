#include <stdio.h>


void sort(char array[], int size){                       // char oldu
    
    for(int i = 0; i <size-1; i++){                    
                                                       
        for(int j= 0; j<size-1; j++){                 

            if(array[j] < array[j+1]){                   // büyükten küçüğe dedik keyfi      

                int temp = array[j];
                array[j] = array[j+1];
                array[j+1] = temp;

            }
        }

    }
}


void print_sort_array(char array[] , int size){         // char oldu

    for(int i = 0; i<size; i+=1){ 
        printf("%c\t", array[i]);                        // %c oldu


    }

    
}



int main(){


    char range[] = {'b','c','d','e','f'};                   // hafrfler verildi
    int size = sizeof(range)/sizeof(range[0]);            

    sort(range,size);
    print_sort_array(range,size);


    return 0;
}