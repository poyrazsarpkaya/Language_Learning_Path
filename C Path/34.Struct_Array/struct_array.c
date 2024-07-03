#include <stdio.h>


 struct channel_list_struct{
    char channel_name[30];
    int  channel_sub;


 };


int main(){

    struct channel_list_struct channel_1 = {"Diomand Tema", 750000};
    struct channel_list_struct channel_2 = {"Deep House", 2000000};
    struct channel_list_struct channel_3 = {"NCS", 10000000};

    struct channel_list_struct youtubers[] = {channel_1, channel_2, channel_3};                 // Yapının içinde  bir Dizin oluşturmuş olduk.

    for(int i = 0; i < sizeof(youtubers)/sizeof(youtubers[0]); i+=1){

        printf("\nChannel: %s \tSubciritions: %d\n", youtubers[i].channel_name, youtubers[i].channel_sub);     

    }

    return 0;
}