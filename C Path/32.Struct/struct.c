#include <stdio.h>
#include <string.h>

struct Airplanes{

    char name[10];                               // Struct: Yapı, bir bellek bloğunda tek bir ad altında fiziksel olarak gruplandırılmış değişkenler tanımlayan veri türüdür.
    int age;                                     // Bir değişkenin özellikleri burada belirleniyor. Yapı oluşturuyoruz.

};



int main(){

    struct Airplanes f_series;                   // f serisinden olan uçağın adı ve yaşı belirlenildi
    struct Airplanes m_series;

    strcpy(f_series.name, "F-16");
    f_series.age = 30;

    strcpy(m_series.name, "M-418");
    m_series.age  = 65;

    printf("%s %d\n", f_series.name, f_series.age);
    printf("%s %d\n", m_series.name, m_series.age);


    return 0;
}