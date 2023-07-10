// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
bool valid(char password);

int main(void)
{
    char password = get_char("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
    }
}

// TODO: Complete the Boolean function below
bool valid(char password)
{
    if(isalnum(password))
    {

    }return true;
    if(isalpha())
    return false;
}
