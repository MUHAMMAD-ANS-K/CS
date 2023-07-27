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
    int sum = 0;
    int num[n_length];
    for(int i = n_length - 1; i >= 0 ; i--)
    {
        num[i] = number % 10;
        number = (number - num[i])/10;
    }
    int y;
    int x = n_length - 2;
    while(x >= 0)
    {
        int z = num[x] * 2;
        if(z > 9)
        {
           y =  z % 10;
           sum+= y;
           z = (z - y)/10;
        }
        sum += z;
        sum += num[x + 1];
        x -= 2;
    }

    printf("%i\n", sum);

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