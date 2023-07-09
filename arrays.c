#include <stdio.h>
#include <cs50.h>

const int N = 3;
float average(int length , int x[]);

int main(void)
{
    int scores[3];
    for (int i = 0; i < N; i++)
    {
        scores[i] = get_int("Number: ");
    }
    printf("Average: %f\n",average(N , scores));
}



float average(int length , int x[])
{
    int sum = 0;
    for(int i = 0; i < length; i++)
    {
        sum += x[i];
    }
    return sum/ (float) N;
}