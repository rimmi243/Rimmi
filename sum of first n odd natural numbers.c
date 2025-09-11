#include<stdio.h>
int main()
{
int n, sum=0, i;
printf("enter the value of n:");
scanf("%d", &n);
for (i=1; i<=n; i++)
{
sum +=(2*i-1);
}
printf("sum of first %d odd natural numbers is: %d\n", n, sum);
return 0;
}
