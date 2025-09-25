#include<stdio.h>
int main()
{
int a,b;
printf("enter a number to be divided:");
scanf("%d",&a);
printf("enter a divisor:");
scanf("%d",&b);
if(a%b==0)
printf("divisible");
else
printf("not divisible");
return 0;
}
