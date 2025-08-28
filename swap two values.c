#include <stdio.h>
int main()
{
    int a,b,c;
    printf("enter first number:");
    scanf("%d",&a);
    printf("enter second number:");
    scanf("%d",&b);
    c=b;
    b=a;
    a=c;
    printf("numbers before swapping: %d %d\n", b,a);
    printf("numbers after swapping: %d %d\n", a,b);
}
