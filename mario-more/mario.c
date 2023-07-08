#include <cs50.h>
#include <stdio.h>

int main(void)
{
    int h;
    do
    {
        h = get_int("Height of Pyramid: ");
    }
    while (h < 1 && h < 9);
}