#include<stdio.h>
int main()
{
int n, sum=0;

printf("enter positive integer:");
scanf("%d", &n);

for(int i=1; i<=n; i++)
{
sum += i;
}
printf("sum of the first %d natural numbers is:%d\n", n, sum);
return 0;
}
