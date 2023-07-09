#include <stdio.h>
#include <cs50.h>
#include <string.h>

int main(void)
{
    string s = get_string("Name: ");
    int n = 0;
    while(s != '\0')
    {
        n++;
    }
    
    printf("%i\n", n);
}