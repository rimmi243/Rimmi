#include <stdio.h>
#include <string.h>

int main()
{
    char str[100];
    int i, len;

    printf("Enter a string: ");
    fgets(str, sizeof(str), stdin);
    str[strcspn(str, "\n")] = '\0';

    len = strlen(str);

    printf("\nReversed string vertically:\n");
    for (i = len - 1; i >= 0; i--)
    {
        printf("%c\n", str[i]);
    }

    return 0;
}
