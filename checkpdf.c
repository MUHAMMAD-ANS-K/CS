#include <stdio.h>
#include <stdint.h>
#include <cs50.h>

int sizeof_buffer = 4;
int main(int argc , string argv[])
{
    if(argc != 2)
    {
        printf("Invalid Input\n");
        return 1;
    }
    string filename = argv[1];
    FILE *file = fopen(filename , "r");
    if(file == NULL)
    {
        printf("File not Found\n");
        return 0;
    }
    uint8_t pdf_digits[] = {37, 80, 68, 70};
    uint8_t buffer[sizeof_buffer];
    fread(buffer ,1 ,4 ,file);
    for(int i = 0; i < sizeof_buffer; i++)
    {
         if(buffer[i] != pdf_digits[i])
        {
            printf("File is likely not a pdf one\n");
             fclose(file);
             return 0;
        }
    }
    printf("Looks like a pdf\n");
    fclose(file);
    return 0;
}