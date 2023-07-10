#include <cs50.h>
#include <stdio.h>
string replace(string s);

int main(int argc, string argv[])
{
    if(argc =! 2)
    {
        printf("Fuck You\n");
        return 1;
    }
    else
    {
        string words = argv[1];
        printf("%s\n",replace(words));
    }
}
string replace(string s)
{
    string n = s
    for(i = 1;i < strlen(s); i++)
    {
     char c = tolower(s);
    switch(c)
    {
        case 'a':
        n[i]= '6';
        break;
        case 'i':
        n[i] = '1';
        break;
        case 'e':
        n[i] = '3';
        break;
        case 'o':
        n[i] = '0';
        break;
        default:
        n[i] = c;
        break;
    }
    }

    return n;
}