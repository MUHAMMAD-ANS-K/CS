#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string s = get_string("Name: ");
    printf("%i %i %i \n", s[0], s[1] ,s[2]);
}