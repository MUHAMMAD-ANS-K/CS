#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int c;
    do
    {
        c = get_int("Size: \n")
    }
    while(c < 0);
     for(int i = 0; i < c; i++)
     {
        for(int j = 0;j < c;j++)
        {
            printf("#")
        }
     }
}