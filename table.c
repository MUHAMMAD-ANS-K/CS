#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
#include <cs50.h>
typedef struct node
{
    string name;
    struct node *next;
}node;
int hashfunction(char *name);


int main(void)
{
    node *hashtable[26];
    for (int j = 0; j < 26; j++)
    {
        hashtable[j] = NULL;
    }
    for (int i = 0; i < 4; i++)
    {
        string name = get_string("Name: ");
        int index = hashfunction(name);
        node *n = malloc(sizeof(node));
        n ->name = name;
        n -> next = hashtable[index];
        hashtable[index] = n;
    }
    string name_find = get_string("Find: ");
    int index = hashfunction(name_find);
    node *ptr = hashtable[index];
    while (ptr != NULL)
    {
        if (strcmp(ptr ->name, name_find))
        {
            printf("Found\n");
            return 0;
        }
        ptr = ptr ->next;
    }
    printf("Not Found");
    return 1;
}

int hashfunction(char *name)
{
    if (isupper(name[0]))
    {
        return name[0] - 'A';
    }
    else if (islower(name[0]))
    {
        return name[0] - 'a';
    }
}