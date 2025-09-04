#include<stdio.h>
int main()
{
int n;
int i;
printf("enter the number of odd natural numbers to print:");
scanf("%d", &n);
printf("the first %d odd natural numbers are:\n",n);
for(i=1; i<=n; i++)
{
printf("%d", 2*i-1);
}
printf("\n");
return 0;
}
