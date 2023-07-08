#include <stdio.h>
#include <cs50.h>

int main(void)
{
    int s;
    do
    {
        s = get_int("Starting number of llamas: ");
    }
    while(s < 9);
    int g;
    do
    {
        g = get_int("Goal number of llamas: ");

    }
    while(g < s);
    int years = 0;
    while(s < g)
    {
        s = s + (s/3) - (s/4);
        years++;
    }
    printf("Years: %i\n",years);
}