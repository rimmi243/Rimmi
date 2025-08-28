#include <stdio.h>
int main()
{
    float b,h,a;
    printf("enter base of triangle:");
    scanf("%f", &b);
    printf("enter height of triangle:");
    scanf("%f", &h);
    a=(b*h)/2.0;
    printf("area of triangle: %f\n", a);
}
