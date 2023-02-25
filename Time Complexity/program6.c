#include <stdio.h>


//What is the time complexity of the following snippet of code?

int isPrime(int n){
    for (int i = 0; i < 1000; i++)
    {
        if (n % i == 0)
        {
            return 0;
        }   
    }
    return 1;
}

int main()
{
    isPrime(18);
    return 0;
}