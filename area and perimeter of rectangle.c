#include <stdio.h>
int main()
{
    int l,b,a,p;
    printf("enter length of rectangle:");
    scanf("%d", &l);
    printf("enter breadth of rectangle:");
    scanf("%d", &b);
    a=l*b;
    printf("area of rectangle: %d\n", a);
    p=2*(l+b);
    printf("perimeter of rectangle: %d\n", p);
}
