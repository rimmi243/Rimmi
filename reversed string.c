#include <stdio.h>
#include <string.h>

int main()
{
    char str[100], rev[100];
    int i, len, j;

    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    str[strcspn(str, "\n")] = '\0';

    len = strlen(str);
    j = 0;


    for (i = len - 1; i >= 0; i--)
    {
        rev[j++] = str[i];
    }
    rev[j] = '\0';
    printf("Reversed string: %s\n", rev);

    return 0;
}
