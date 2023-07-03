#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string name = get_string("Name: ");
    string age = get_string("Age: ");
    string number = get_string("Number: ");
    printf("%s %s %s\n",name,age,number);
    }