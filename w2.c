#include <stdio.h>
#include <cs50.h>

int main(void)
{
    do
    {
        int n = get_int("Size of Array: ");
    }

    int array[n];
    array[0] = 1;
    for (int i = 1; i < n; i++)
    {
        array[i] = array[i - 1]* 2;
        printf("%i\n", array[i - 1]);
    }


}