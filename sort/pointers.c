#include <stdio.h>

int main(void)
{
    FILE *ptr = fopen("sorted5000.txt", "r");

    int array_size = 5000;
    int array[array_size];
    fread(array, sizeof(int), 5000 , ptr);

    for(int i = 0; i < array_size; i++)
    {
    printf("%i\n", array[i]);
    }
    fclose(ptr);
}