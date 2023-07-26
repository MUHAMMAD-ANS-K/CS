#include <stdio.h>

int main(void)
{
    FILE *ptr = fopen("txt1.csv", "r");

    int array_size = 10;
    int array[array_size];
    fread(array, sizeof(int), 10 , ptr);

    for(int i = 0; i < array_size; i++)
    {
    printf("%i\n", array[i]);
    }
    fclose(ptr);
}