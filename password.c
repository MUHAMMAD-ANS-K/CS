// Check that a password has at least one lowercase letter, uppercase letter, number and symbol
#include <cs50.h>
#include <stdio.h>
#include <ctype.h>
#include <string.h>

bool valid(string password);

int main(void)
{
    string password = get_string("Enter your password: ");
    if (valid(password))
    {
        printf("Your password is valid!\n");
    }
    else
    {
        printf("Your password needs at least one uppercase letter, lowercase letter, number and symbol\n");
    }
}
//islower(password[i]) && isupper(password[i]) && isdigit(password[i])

// TODO: Complete the Boolean function below
bool valid(string password)
{
    bool check_upper = false;
    bool check_lower = false;
    bool check_symbol = false;
    bool check_digit = false;
    for(int i = 0; i < strlen(password); i++)
    {
       if(ispunct(password[i]))
       {
        check_symbol = true;
       }
       if(islower(password[i]))
       {
        check_lower = true;
       }
       if(isupper(password[i]))
       {
        check_upper = true;
       }
       if(isdigit(password[i]))
       {
        check_digit = true;
       }
    }

    return false;
}
