#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //This part prompts the user for starting number of llamas and reprompts in case of invalid input.
    int s;
    do
    {
        s = get_int("Starting number of llamas: ");
    }
    while (s < 9);
    //This part prompts the user for ending number of llamas and reprompts in case of invalid input.
    int g;
    do
    {
        g = get_int("Goal number of llamas: ");

    }
    while (g < s);
    //This part calculates year to reach goal number of llamas and prints them to the screen.
    int years = 0;
    while (s < g)
    {
        s = s + (s / 3) - (s / 4);
        years++;
    }
    printf("Years: %i\n", years);
}