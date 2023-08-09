#include <stdio.h>
#include <cs50.h>
#include <string.h>
int main(void)
{
    string a = get_string(": ");
    string b = get_string(": ");
    if (strcmp(a,b) == 0)
    {
        printf("Equal");
    }
}