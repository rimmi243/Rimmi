#include<stdio.h>
int main()
{
int a,b;
printf("enter the number to be separated:\n");
scanf("%d",&a);
for(a;a>0;)
{
b=a%10;
a=a/10;
printf("%d\t",b);
}
return 0;
}
