#include <stdio.h>

//Calucate the time complexity of the program
void func(int n){
    int sum = 0;
    int product = 1;

    // contains two for loop -- k2
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            printf("%d, %d\n",i,j);
        }
    }
    /*
    So, we can see and understand that it will go like this
    talking about k2n as it is dominating factor.
    Tn = n + n + n + ....... 1 
        = n(1+1+1+.......1)// so this will n^2 which means it is k2n^2
        = On^2
    */
}

int main()
{
    func(8);    
    return 0;
}