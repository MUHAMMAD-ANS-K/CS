#include <cs50.h>
#include <stdio.h>

int main(void)
{
    long number = get_long("Number: ");
    int num;
    int sum = 0;
    while(number > 0)
    {
        num = number % 10;
        number = (number - num)/10;
        sum += num*2;
    }
    printf("%i\n", sum);

}