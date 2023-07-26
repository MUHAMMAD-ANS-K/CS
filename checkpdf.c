#include <stdio.h>
#include <stdint.h>
#include <cs50.h>
int main(int argc , string argv[])
{
    if(argc != 2)
    {
        printf("Invalid Input\n");
        return 1;
    }
    string filename = argv[1];
    FILE *file = fopen(filename , "r");
    fclose(file);
}