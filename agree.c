#include <cs50.h>
#include <stdio.h>

int main(void)
{
    char c = get_char("Do you agree?\n");

    if(c == 'y' || c == 'Y')
    {
        printf("Agreed\n");
    }
    else if(c == 'n' || c == 'N')
    {
        printf("Not Agreed\n");
    }
}wget https://cdn.cs50.net/2022/fall/labs/1/debug.c//