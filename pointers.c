#include <stdio.h>

int main(void)
{
    FILE *ptr = fopen("txt1.csv", "r");
    char c;
    while((c = fgetc(ptr))!= EOF)
    {
    printf("%c",c);
    }
    printf("\n");
    fclose(ptr);
    int s = -1;
    while(s < 0)
    {
    printf("S: ");
    scanf("%i", &s);
    printf("S is %i", s);
    }

}