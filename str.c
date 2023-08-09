#include <stdio.h>
#include <stdlib.h>
int main(void)
{
    char *s = malloc(10 * sizeof(char));
    printf("Name: ");
    scanf("%s",s);
    printf("%s",s);
    free(s);
}