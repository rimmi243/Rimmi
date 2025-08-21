#include<stdio.h>
void main()
{
int a,b;
printf("enter the first number");
scanf("%d", &a);
printf("enter the second number");
scanf("%d", &b);
if(a>b)
{
printf("the larger number is: %d\n", a);
printf("the smaller number is: %d\n", b);
}
else
{
printf("the larger number is: %d\n", b);
printf("the smaller number is: %d\n", a);
}
}
