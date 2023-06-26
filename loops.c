#include <stdio.h>
#include <cs50.h>

int main(void)
{
   const int n = 5;
   for(int i = 0; i < n; i++)
   {
    printf("#");
    for(int j = 0; j < n; j++)
    {
        printf("#");
    }
    printf("\n");
   }
   int c;
   do
   {
        c = get_int("Size: ");
   }
   while(c < 3);
}
