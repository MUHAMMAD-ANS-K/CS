#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int h;
    do
    {
        h = get_int("Height of Pyramid: ");
    }
    while (h > 8 || h < 2);
 for(int i = 0; i < h; i++)
    {

 
        printf("  ");
        for(int k = 0;k <= i; k++)
        {
            printf("#");
        }
     printf(" \n");
    }
}
