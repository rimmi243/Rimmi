#include<stdio.h>
void main()
{
int a[10];
int i;

for(int i=0;i<10;i++)
{
printf("enter value %d:\n",i+1);
scanf("%d", &a[i]);
}
printf("4th value is: %d\n",a[3]);
printf("7th value is: %d\n",a[6]);
printf("9th value is: %d\n",a[8]);
}
