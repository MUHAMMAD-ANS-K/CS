#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int x = get_int("x: \n");
    int y = get_int("y: \n");
    printf("%i",x + y);
}