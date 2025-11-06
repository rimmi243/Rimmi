#include <stdio.h>


int sumofdigits(int num)
{

    if (num == 0)
    {
        return 0;
    }

    else
    {
        return (num % 10) + sumofdigits(num / 10);
    }
}

int main()
{
    int number;

    printf("Enter a number: ");
    scanf("%d", &number);

    int sum = sumofdigits(number);

    printf("Sum of digits of %d = %d\n", number, sum);

    return 0;
}
