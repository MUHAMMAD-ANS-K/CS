#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
int count_letters(string txt);
int count_words(string txt);

int main(void)
{
    string text = get_string("Text: ");
    printf("%i   %i\n", count_letters(text), count_words(text));
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


int count_words(string txt)
{
    int wrd = 0;
    for(int k = 0; k < strlen(txt); k++)
    {
        if(isspace(txt[k]))
        {
            wrd++;
        }
    }
    return wrd;
}

int count_sentences(string txt)
{
    int sntns = 0;
    for(int j = 0; j < strlen(txt); j++)
    {
        if(ispunct(txt[j]))
        {
            sntns++;
        }
    }
    return sntns;
}