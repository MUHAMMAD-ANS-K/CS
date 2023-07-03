#include <stdio.h>
#include <cs50.h>
int get_size(void);
void printgrid(int size);

int main(void)
{
    int n = get_size();
    printgrid(n);
}


int get_size(void)
{
    int c;
    do
    {
        c = get_int("Size: ");
    }
    while(c < 0);
    return c;
}
void printgrid(int size)
{
    for(int i = 0;i < size;i++)
    {
        for(int j = 0;j < size;j++)
        {
            printf("#");
        }printf("\n");
    }
}










