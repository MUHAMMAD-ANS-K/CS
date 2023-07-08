#include <stdio.h>
#include <cs50.h>

int main (void)
{
    int h = get_int("Height: ");
    for(int i = 0; i < h; i++)
    {
       for(int j = h; j > i;j--)
        {
            printf(" ");
        }
        for(int k = 0; k <= i; k++)
        {
            printf("#");
        }
        printf("\n");
    }
}