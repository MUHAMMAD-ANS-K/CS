#include <cs50.h>
#include <stdio.h>
int number_length(long number);

int main(void)
{
    long number = get_long("Number: ");
    int n_length = number_length(number);
    if(n_length < 13)
    {
        printf("INVALID\n");
        return 1;
    }
    int num[n_length];
    for(int i = n_length - 1; i >= 0 ; i--)
    {
        num[i] = number % 10;
        number = (number - num[i])/10;
    }
    for(int j = n_length - 2;  )
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