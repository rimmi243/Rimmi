#include <stdio.h>
int main()
{
    float a,b,c;
    printf("enter currency in dollars:");
    scanf("%f",&a);
    b=a*48.0;
    printf("currency in rupees is: %f\n",b);
    c=b/70.0;
    printf("currency in pounds is: %f\n",c);
}
