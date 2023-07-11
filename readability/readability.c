#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
int count_letters(string txt);

int main(void)
{
    string text = get_string("Text: ");
    printf("%i\n", count_letters(text));
}


int count_letters(string txt)
{
    int ltrs = 0;
    for(int i = 0; i < strlen(txt); i++)
    {
        if(isalnum(txt[i])){
            ltrs++;
        }
    }
    return ltrs;
}