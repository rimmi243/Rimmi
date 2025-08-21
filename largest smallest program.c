#include<stdio.h>
void main()
{
int a,b,c;


printf("enter three numbers");
scanf("%d %d %d", &a, &b, &c);

if(a>b && a>c)
printf("largest is: %d\n", a);

else if(b>a && b>c)
printf("largest is: %d\n", b);

else
printf("largest is: %d\n", c);
}
