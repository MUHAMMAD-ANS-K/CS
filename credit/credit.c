#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long number = get_long("Number: ");
    int num = number % 10;
    printf("%i\n", num);

}