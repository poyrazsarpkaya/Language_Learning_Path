#include <stdio.h>

int main (){

    int svrch[2][3] = {{3,4,5},{7,8,9}};          // bu şekilde satır ve sütün tanımı yapılıyor. yan yana yani görsel olrak satır satır yazılıyor.
                                                  // kaç tane olduklarını değişken atarken yazıyoruz. int svrch[2][3]
    printf("%d\n", svrch[0][2]);
    



    int ch[2][3];                                // kaçınıcı dizinde olduğu 0 dan başlar ancak Kaç tane olduğu (size) 1 den başlar. 2 satırımız 3 sütunumuz var

    ch[0][0] = 5;
    ch[0][1] = 10;
    ch[0][2] = 15;
    ch[1][0] = 20;
    ch[1][1] = 25;
    ch[1][2] = 30;

    //printf("\n%d", ch[0][1]);
 
    int rows = sizeof(ch)/sizeof(ch[0]);                   //  Toplam boyutu 0. satırdaki boyuta böldük. Satır sayısını bulduk
    int columns  = sizeof(ch[0])/sizeof(ch[0][1]);         //  Satırdaki toplam boyutu, o satırın herhangibir sütünundaki karakterin boyutuna bölünce sütun sayısını bulduk

 
    for( int i = 0; i<rows; i++){

        for( int j = 0; j<columns; j++){
            printf("%d ", ch[i][j]);

        }
    printf("\n");
    }



    return 0;
}