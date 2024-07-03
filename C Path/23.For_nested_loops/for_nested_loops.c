#include <stdio.h>

int main(){

    int rows;
    int columns;
    char symbol;
    char space;


    printf("\nSatir saiyisini giriniz ");
    scanf("%d", &rows);
    printf("\nSutun sayisini giriniz: ");
    scanf("%d", &columns);                               // iki defa üst üste input aldıktan sonra arabellekte yeni satır karakteri oluşturuluyor. bu yeni satır da sonraki inputun değeri oluyor

    scanf("%c", &space);                                 // Bunu önlemek için sonraki inputun karakter değeri (%c) ile aralarına bir scanf daha koyuyoruz. O boşluk değeri bun değişkene atanmış oluyor ;)

    printf("\nKarakter giriniz: ");
    scanf("%c", &symbol);

  
    for(int i =1; i<=rows; i++){                        // satır satır yazacağız dedik

        for(int j=1; j<=columns; j++){                  // sütunları satır değerleri ile doldurduk. tek tek satır atlayarak
            printf("%c", symbol);


        }
    printf("\n");                                       // bir sonraki satıra geçtik

    }


    return 0;
}