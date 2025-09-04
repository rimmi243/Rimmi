#include<stdio.h>
int main()
{
int n,i;
int isPrime=1;
printf("enter a number:");
scanf("%d",&n);
if(n<=1)
{
isPrime=0;
}
for(i=2;i<n;i++)
{
if(n%i==0)
{
isPrime=0;
break;
}
}
if(isPrime==1)
{
printf("%d is a prime number\n",n);
}
else
{
printf("%d is not a prime number\n",n);
}
return 0;
}
