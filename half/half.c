#include <cs50.h>
#include <stdio.h>

float half(float bill, float tax, float tip);

int main(void)
{
    float bill_amount = get_float("Bill before tax and tip: ");
    float tax_percent = get_float("Sale Tax Percent: ");
    float tip_percent = get_int("Tip percent: ");

    printf("You will owe %.2f each!\n", half(bill_amount, tax_percent, tip_percent));
}



float half(float bill, float tax, float tip)
{
    bill = bill/2;
    bill += (tax/100) * bill + (tip/100) * bill;
    return bill;
}
