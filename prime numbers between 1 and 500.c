#include<stdio.h>
int main()
{
int n,i,isPrime;

printf("prime numbers between 1 and 500 are:\n");
for(n=2;n<=500;n++)
{
isPrime=1;
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
    printf("%d",n);
}


}
return 0;
}
