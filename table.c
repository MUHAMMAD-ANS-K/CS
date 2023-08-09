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
        string name = malloc(sizeof(string));
        printf("Name: ");
        scanf("%s",name);
        int index = hashfunction(name);
        node *n = malloc(sizeof(node));
        n ->name = name;
        free(name);
        n -> next = hashtable[index];
        hashtable[index] = n;
    }
    string name_find = malloc(sizeof(string));
    if (name_find == NULL)
    {
        return 1;
    }
    printf("Find: ");
    scanf("%s",name_find);
    int index = hashfunction(name_find);
    node *ptr = hashtable[index];
    while (ptr != NULL)
    {
        if (strcmp(ptr->name, name_find) == 0)
        {
            printf("Found\n");
            break;
        }
        ptr = ptr ->next;
    }
    free(name_find);
    for(int i = 0; i < 26; i++)
    {
        ptr = hashtable[i];
        while(ptr != NULL)
        {
            node *next = ptr -> next;
            free(ptr);
            ptr = next;
        }
    }

}

int hashfunction(char *name)
{
    if (isupper(name[0]))
    {
        return name[0] - 'A';
    }
    return name[0] - 'a';
}