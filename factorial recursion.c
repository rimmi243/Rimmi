#include<stdio.h>
int factorial(int n)
{
if(n==0||n==1)
return 1;
else
return n*factorial(n-1);
}
int main()
{
int num;
printf("enter a number:");
scanf("%d",&num);
printf("factorial of %d is: %d\n", num, factorial(num));
return 0;
}
