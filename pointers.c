#include <stdio.h>

int main(void)
{
    FILE *ptr = fopen("txt1.csv", "r");
    char c;
    while((c = fgetc(ptr))!= EOF)
    {
    printf("%c\n",c);
    }
    fclose(ptr);

}