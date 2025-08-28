#include<stdio.h>
int main()
{
    float bytes,KB,MB,GB;

     printf("enter the number of bytes:");
     scanf("%f", &bytes);

     KB = bytes /1000;
     MB = bytes /1000000;
     GB = bytes /1000000000;

     printf("your given bytes converted into KB %f\n ", KB);
     printf("your given bytes converted into MB %f\n ", MB);
     printf("your given bytes converted into GB %f\n ", GB);

return 0;
}
