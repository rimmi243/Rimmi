#include<stdio.h>
int main()
{
      int a[]={500,200,100,50,20,10,5,2,1},n,i,c[9];
      printf("enter an amount:\n");
      scanf("%d",&n);
      for(i=0;i<9;i++)
      {
         c[i]=0;
      }
      i=0;
         while(n>0)
         {
         if(n>=a[i])
             {
              n=n-a[i];
              c[i]=c[i]+1;
             }
             else if(i>8)
             {break;}
             else
             {
                i=i+1;
             }
         }
         for(i=0;i<9;i++)
         {
         printf("%d=%d\n",a[i],c[i]);
         }
}

