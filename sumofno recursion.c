#include<stdio.h>
void main()
{
int sumofno(int);
printf("%d",sumofno(3));
}
int sumofno(int n)
{
if (n==0)
return 0;
else
return(n+sumofno(n-1));
}
