#include <stdio.h>
#include <stdlib.h>

int main(void)
{
    char *s = malloc(10 * sizeof(char));
    printf("S: ");
    scanf("%s", s);
    printf("%s\n",s);
    free(s);
    int x = 90;
    int *y = &x;
    printf("%i\n", *y);
}