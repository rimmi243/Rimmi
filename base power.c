#include <stdio.h>


int power(int a, int b)
{
    int result = 1;
    for (int i = 1; i <= b; i++)
    {
        result = result * a;
    }
    return result;
}

int main()
{
    int a, b;

    printf("Enter the base number (a): ");
    scanf("%d", &a);
    printf("Enter the exponent (b): ");
    scanf("%d", &b);

    printf("\n%d raised to the power %d is: %d\n", a, b, power(a, b));

    return 0;
}
