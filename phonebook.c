#include <stdio.h>
#include <cs50.h>
#include <string.h>
const int n = 2;

typedef struct
{
    string name;
    string number;
}
person;
int main(void)
{
    person people[n];
    people[0].name = "David";
    people[0].number = "+1-876-543-2109";
    people[1].name = "Carter";
    people[1].number = "+1-543-219-8765";
    string s = get_string("Name: ");
    for(int i = 0; i < n; i++)
    {
        if(strcmp(people[i].name , s) == 0)
        {
            printf("Found: %i", people[i].number);
        }
    }
    if(strcmp(people[i].name , s) =! 0)
    {
        printf("Not Found");
    }
    printf("\n");
}