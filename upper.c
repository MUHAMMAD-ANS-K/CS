#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string s = get_string("Before: ");
    printf("After: ");
    int n = 0;
    while(s[n] != '\0')
    {
        n++;
    }
    for(int i = 0; i < n; i++)
    {
        if(s[i] >= 'a' && s[i] <= 'z')
        {
            printf("%c",s[i] - 32);
        }
        else
        {
            printf("%c", s[i]);
        }
    }printf("\n");
}