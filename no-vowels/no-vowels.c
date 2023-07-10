#include <cs50.h>
#include <stdio.h>
string replace(string s[1]);

int main(int argc, string argv[])
{
    if(argc == 1)
    {
        printf("Fuck You\n");
        return 1;
    }
    else
    {
        printf("%s\n",replace(argv));
    }
}
string replace(string s[1])
{
    switch(s[1])
    {
        case a:
        printf("6");
        break;
        case i:
        printf("1");
        break;
        case e:
        printf("3");
        break;
        case o:
        printf("0");
        break;
        default:
        printf("%s", s[1]);
        break;
    }
    return s[1];
}