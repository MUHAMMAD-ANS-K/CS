#include <stdio.h>
#include <cs50.h>

int main(void)
{
    string name = get_string("Name: ");
    int age = get_int("Age: ");
    string number = get_string("Number: ");
    printf("%s %i %s\n",name,age,number);
    }