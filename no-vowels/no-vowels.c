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
    
    for(i = 1;i < strlen(s); i++)
    {

    }
    switch(s[1])
    {
        case 'a':
        printf("6");
        break;
        case 'i':
        printf("1");
        break;
        case 'e':
        printf("3");
        break;
        case 'o':
        printf("0");
        break;
        default:
        printf("%s", s[1]);
        break;
    }
    return s[1];
}