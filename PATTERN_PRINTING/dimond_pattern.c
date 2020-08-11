// diamond pattern
// first: print normal triangle
// second: print inverted triangle

//    *
//   * *
//  * * *
//   * *
//    *

#include <stdio.h>

int main()
{
    int n,i,j,k;
    // i for row
    // j for col 
    // k for number of spaces
    scanf("%d",&n);
    // printing upright odd pyramid or triangle
    for(i=0;i<n;i++)
    {
        for(k=i;k<n;k++)
            printf(" ");
        for(j=0; j<(2*(i+1))-1; j++)
            printf("*");
        printf("\n");
    }

    //printing inverted odd pyramid or triangle
    for(i=n-1;i>0;i--)//i 3,2,1 // only change here
    {   printf(" ");
        for(k=i;k<n;k++) //k 0,1,2 spaces
        printf(" ");
        for(j=0;j<2*i-1;j++)// j loops 5 3 1
        printf("*");
    printf("\n");
    }
    return 0;
}