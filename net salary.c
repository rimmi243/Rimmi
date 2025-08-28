#include <stdio.h>
int main()
{
    float a,b,c,d;
    printf("enter value of gross salary:");
    scanf("%f", &a);
    b=0.1*a;
    printf("allowance is: %f\n", b);
    c=0.03*a;
    printf("deductions are: %f\n", c);
    d=a+b-c;
    printf("net salary is: %f\n", d);
}
