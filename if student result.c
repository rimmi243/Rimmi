#include<stdio.h>
void main()
{
float a,b,c,d;
printf("enter marks scored in maths:");
scanf("%f", &a);
printf("enter marks scored in chemistry:");
scanf("%f", &b);
printf("enter marks scored in physics:");
scanf("%f", &c);
d=(a+b+c)/3;
if(a<35||b<35||c<35)
{
printf("the student failed");
}
else if(d>=70)
{
printf("the student scored distinction");
}
else if(d>=60)
{
printf("the student scored first");
}
else if(d>=50)
{
printf("the student scored second");
}
else
{
printf("the student scored third");
}
}
