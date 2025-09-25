#include<stdio.h>
int main()
{
int a[5];
int i,j,t;
printf("enter an array:\n");
for(i=0;i<5;i++)
{
scanf("%d",&a[i]);
}
for(i=0;i<4;i++)
{
for(j=0;j<4;j++)
{
if(a[j]<a[j+1])
{
t=a[j];
a[j]=a[j+1];
a[j+1]=t;
}
}
}
printf("sorted array:\n");
for(i=0;i<5;i++)
{
printf("%d\t",a[i]);
}
printf("\n");
return 0;
}
