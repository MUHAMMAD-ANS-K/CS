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
        for(int j = 0;j < h; j++)
        {
            printf(" #");
        }
     printf(" \n");
    }
}
