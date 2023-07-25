#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char *s = malloc(10);
    printf("S: ");
    scanf("%s", s);
    printf("%s\n",s);
    free(s);
}