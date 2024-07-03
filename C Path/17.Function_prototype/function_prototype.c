#include <stdio.h>

void entry(char x[], char y[]);                       // çalışması istenilen fonksiyom main fonksiyonun altına yazılır ve üst kısma prototipi yani istenilen değerler yazılı
                                                      // Bu sayede aşağıdaki gibi eksik girilen fonksiyonlar olunca error verir. Çalışmaya devam ETMEZ!
int main (){

    char nm[15];
    char cde[15];

    printf("Please enter the name: \n");
    scanf("%s", &nm);
    printf("Please enter the code name: \n");
    scanf("%s", &cde);

    entry(nm);                                         // Burası eksik. kod adı alınmamış

    return 0;
}


void entry(char name[], char code_name[]){

    printf("Welcome to Matrix main base, agent %s\n", name);
    printf("Code name accepted! %s", code_name);

}