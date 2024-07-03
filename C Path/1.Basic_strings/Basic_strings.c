#include<stdio.h>                                                     // Standart input output h(hexadecimal)


int main(){                                                           // int ile tanımlıyoruz fonksiyonu çünkü 0 döndürüyor

    printf("Welcome to matrix\n");                                    // \n gelecek metnin alt satıra geçmesi için  
    printf("Follow the rabbit\n");
    
    /* 
    Çoklu yorum satırı için
    
    
    */


    printf("3\t\t\t4\t\t\t5\t\t\t6\n");                                                           //  \t yatay sekme 
    printf("3\v4\v5\v6\v7");                                                                      //  \v dikey sekme. aşağıya doğru maddeler halinde sekmelere ayırır ve geri kalan yazı da o hizadan DEVAM EDER!
    printf("\b");                                                                                 //  \b geri tuşu.  sondan bir önceki karaktere kadar gösterilmesini sağlar
    printf("\e");                                                                                 //  \e kaçış karakteri. Bir sonraki karakteri es geçer
    printf("\a");                                                                                 //  \a uyarı
    printf("\r");                                                                                 //  \r Satır Başı. Satır başı olduğu zaman öneceki tüm çıktılar görülmeyebiliyor for döngüsünde öyle!!
    printf("\"Gözüm herşeyi görmüşsün ama ses yok senden boş yere gördün\" - Motive\n");          //  Metin içerisinde " ile bir şey yazakcak  " öncesi \ kullanılmalı
    printf("\\");                                                                                 //  \\ Ters slash(\)
    printf("\'");                                                                                 //  \' tek tırnak
    printf("\"");                                                                                 //  \" Çift Tırnak
    printf("\?");                                                                                 //  \? Soru işareti
    printf("\f");                                                                                 //  \f Form besleme sayfa sonu. sayfayı bitirir ve  Bir satır boş bırkaır


    return 0;                                                                                     // Program hatasız sonlandırıldı demektir. (Program çalıştırılmaya başladığında önceden yaratılması gereken objelere ilişkin yapılması gereken işler ve fonksiyonlar çağırıldıktan sonra) main fonksiyonunu işletim sistemi çağırır ve program sonlandığında main fonksiyonunun geri dönüş değerinin hedefi de yine kendisini çağırmış olan işletim sisteminin kendisidir.
}                                                                                                 // 0 döndürdüğü için fonksiyonu belirlerken int kullanıypruz :)