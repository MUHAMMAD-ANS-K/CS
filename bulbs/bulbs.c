#include <cs50.h>
#include <stdio.h>
#include <string.h>
#include <cs50.h>
#include <stdlib.h>

const int BITS_IN_BYTE = 8;

void print_bulb(int bit);

int main(void)
{
    int bits[8];
    string text = get_string("Message: ");
    int number[strlen(text)];
    for(int i = 0; i < strlen(text); i++)
    {
        number[i] = text[i];
        for(int j = 7; j >= 0; j--)
        {
            bits[j] = number[i] % 2;
            number[i] = number[i] / 2;
        }
        for(int k = 0; k < 8; k++)
        {
            printf("%i",bits[k]);
        }
    }
    printf("\n");
}

void print_bulb(int bit)
{
    if (bit == 0)
    {
        // Dark emoji
        printf("\U000026AB");
    }
    else if (bit == 1)
    {
        // Light emoji
        printf("\U0001F7E1");
    }
}

        //while(number[i] > 0)
        //{
          //  bits[i] = number[i] % 2;
        //}
        //printf("%i", bits[i]);