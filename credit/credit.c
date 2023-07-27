#include <cs50.h>
#include <stdio.h>
int number_length(long number);

int main(void)
{
    long number = get_long("Number: ");
    int num;
    int n_length = number_length(number);

   // for(int )
    //number = (number - num)/10;
    int sum = 0;
    printf("%i\n", n_length);

}

int number_length(long number)
{
    int count = 0;
    while (number > 0)
    {
       number =  number/10;
        count += 1;
    }
    return count;
}