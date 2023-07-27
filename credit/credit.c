#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long number = get_long("Number: ");
    int num;
    int sum = 0;
    while(number > 0)
    {
        num = number % 100;
        number = (number - num)/100;
        sum += num*2;
    }
    printf("%i\n", sum);

}