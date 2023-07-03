#include <stdio.h>
#include <cs50.h>
int get_size(void);
void printgrid(size);

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
}
void printgrid(size)
{
    for(i = 0;i < c;i++)
    {
        for(j = 0;j < c;j++)
        {
            printf("#");
        }printf("\n");
    }
}










