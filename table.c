#include <stdio.h>
#include <stdlib.h>
#include <ctype.h>
#include <string.h>
typedef char * string;
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
        string name = NULL;
        printf("Name: ");
        scanf("%s",name);
        printf("%s\n",name);
        int index = hashfunction(name);
        node *n = malloc(sizeof(node));
        n ->name = name;
        n -> next = hashtable[index];
        n = hashtable[index];
    }
    string name_find = NULL;
    printf("Find: ");
    scanf("%s",name_find);
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
    return toupper(name[0]) - 'A';
}