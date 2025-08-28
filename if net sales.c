#include<stdio.h>
void main()
{
float a,b,c;
printf("enter gross sales:");
scanf("%f", &a);

if(a>20000)
{
b=0.15*a;
c=a-b;
}
else if(a>10000)
{
b=0.1*a;
c=a-b;
}
else
{
b=0.05*a;
c=a-b;
}
printf("the net sales is: %f", c);
}
