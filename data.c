#include <stdio.h>
#include <stdlib.h>

typedef struct node
{
    int number;
    struct node *next;
}node;
int main(int argc, char *argv[])
{
    node *list = NULL;
    for(int i = 1; i < 4; i++)
    {
        int number = atoi(argv[i]);
        node *n = malloc(sizeof(node));
        if(n == NULL)
        {
            return 1;
        }
        n -> number = number;
        n -> next = NULL;

        n -> next = list;
        list = n;
    }
    for(node *ptr = list; ptr != NULL; ptr = ptr -> next)
    {
        printf("%i\n", ptr -> number);
        free();
    }
}