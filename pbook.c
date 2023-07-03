#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string name = get_string("Name: ");
    string age = get_string("Age: ");
    int number = get_int("Number: ");
    printf("%s %s %i\n",name,age,number);
    }