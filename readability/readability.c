#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <ctype.h>
int count_letters(string txt);
int count_words(string txt);
int count_sentences(string txt);

int main(void)
{
    string text = get_string("Text: ");
    float L = (count_letters(text)/(float) count_words(text)) * 100;
    float S = (count_sentences(text)/(float) count_words(text)) * 100;
    int index = 0.0588 * L - 0.296 * S - 15.8;
    if(index < 1)
    {
        printf("Before Grade 1\n");
    }
    else if(index < 16)
    {
        printf("Grade %i\n",index);
    }
    else if(index >= 16)
    {
        printf("Grade 16+\n");
    }

}


int count_letters(string txt)
{
    int ltrs = 0;
    for(int i = 0; i < strlen(txt); i++)
    {
        if(isalnum(txt[i]))
        {
            ltrs++;
        }
    }
    return ltrs;
}


int count_words(string txt)
{
    int wrd = 1;
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
        if(txt[j] == '!' || txt[j] == '.' || txt[j] == '?')
        {
            sntns++;
        }
    }
    return sntns;
}