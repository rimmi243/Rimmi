#include<stdio.h>
int main()
{
        int a[4][4],b[4][4];
        for(int i=0;i<4;i++)
        {
             for(int j=0;j<4;j++)
             scanf("%d",&a[i][j]);
        }
        for(int i=0;i<4;i++)
        {
             for(int j=0;j<4;j++)
             b[i][j]=a[j][i];
        }
        for(int i=0;i<4;i++)
        {
            for(int j=0;j<4;j++)
            printf("%d\t",b[i][j]);
        }

}
