#include <stdio.h>
#include <cs50.h>
void print_rightpyramid(int height);

int main (void)
{
    int h = get_int("Height: ");
    print_rightpyramid(h);
}








void print_rightpyramid(int height)
{
    for(int i = 0; i < height; i++)
    {
       for(int j = height; j > i;j--)
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