#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string s = get_string("Name: ");
    printf("%i\n", sterlin(s));
}