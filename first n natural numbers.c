#include<stdio.h>
int main()
{
int n;
int i;
printf("enter the numbers of natural numbers to print:");
scanf("%d", &n);
printf("the first %d natural numbers are:\n");
for(i=1; i<=n; i++)
{
printf("%d", i);
}
printf("\n");
return 0;
}
