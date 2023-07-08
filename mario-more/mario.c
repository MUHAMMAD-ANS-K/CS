#include <cs50.h>
#include <stdio.h>

void print_leftpyramid(int height);

int main(void)
{
    int h;
    do
    {
        h = get_int("Height of Pyramid: ");
    }
    while (h > 8 || h < 2);
    print_leftpyramid(h);
}

































void print_leftpyramid(int height)
{
 for(int i = 0; i < height; i++)
    {
        printf("  ");
        for(int k = 0;k <= i; k++)
        {
            printf("#");
        }
     printf(" \n");
    }
}
