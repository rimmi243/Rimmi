#include <stdio.h>
int main()
{
    float a,b,c;
    printf("enter value of gross sales:");
    scanf("%f", &a);
    b=0.1*a;
    c=a-b;
    printf("net sales is: %f\n", c);
}
