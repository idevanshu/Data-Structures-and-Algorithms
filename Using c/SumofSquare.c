#include <stdio.h>
#include <math.h>


int judgeSquareSum(int c) {
    double i = 0;
    int j = sqrt(c);
    while (i <= j) {
        if (i*i + j*j == c)
            return 1;
        else if (i*i + j*j < c)
            i++;
        else
            j--;
    }
    return 0;
}

int main()
{
    int num;
    printf("Enter the number: ", num);
    scanf("%d",&num);
    
    if (judgeSquareSum(num))
    {
        printf("True");
    }else{
        printf("False");
    }
    
    return 0;
}


