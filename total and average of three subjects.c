#include <stdio.h>
int main()
{
    int m,p,c,t,a;
    printf("enter marks in maths:");
    scanf("%d", &m);
    printf("enter marks in physics:");
    scanf("%d", &p);
    printf("enter marks in chemistry:");
    scanf("%d", &c);
    t=m+p+c;
    a=t/3;
    printf("total marks obtained is: %d\n",t);
    printf("average of three subjects is: %d\n",a);
}
