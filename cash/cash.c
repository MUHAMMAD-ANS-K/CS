#include <cs50.h>
#include <stdio.h>

int get_cents(void);
int calculate_quarters(int cents);
int calculate_dimes(int cents);
int calculate_nickels(int cents);
int calculate_pennies(int cents);

int main(void)
{
    // how many cents the customer is owed
    int cents = get_cents();

    // The number of quarters to give the customer
    int quarters = calculate_quarters(cents);
    cents = cents - quarters * 25;

    // The number of dimes to give the customer
    int dimes = calculate_dimes(cents);
    cents = cents - dimes * 10;

    // The number of nickels to give the customer
    int nickels = calculate_nickels(cents);
    cents = cents - nickels * 5;

    // The number of pennies to give the customer
    int pennies = calculate_pennies(cents);
    cents = cents - pennies * 1;

    // Sum coins
    int coins = quarters + dimes + nickels + pennies;

    // Total number of coins to give the customer
    printf("%i\n", coins);
}

int get_cents(void)
{
    int cents;
    do
    {
        cents = get_int("Cents: ");
    }
    while (cents < 0);
    return cents;
}

int calculate_quarters(int cents)
{
    int quarters = 0;
    while (cents > 24)
    {
        cents -= 25;
        quarters++;
    }
    return quarters;
}

int calculate_dimes(int cents)
{
    int dimes = 0;
    while (cents > 9)
    {
        cents -= 10;
        dimes++;
    }
    return dimes;
}

int calculate_nickels(int cents)
{
    int nickels = 0;
    while (cents > 4)
    {
        cents -= 5;
        nickels++;
    }

    return nickels;
}

int calculate_pennies(int cents)
{
    int pennies = 0;
    while (cents > 0)
    {
        cents -= 1;
        pennies++;
    }
    return pennies;
}
