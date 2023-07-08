#include <stdio.h>
#include <cs50.h>
void print_rightpyramid(int n);

int main (void)
{
    int h = get_int("Height: ");
    print_rightpyramid(h);
}








void print_rightpyramid(int n)
{
    for(int i = 0; i < n; i++)
    {
       for(int j = n; j > i;j--)
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