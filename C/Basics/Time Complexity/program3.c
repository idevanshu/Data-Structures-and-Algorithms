#include <stdio.h>
#include <stdlib.h>

int random(int n){
    int number = (rand() % (n+1));
    return number;
}
// Consider the recursive algorithm below, where random(int n) spends one unit of time to return a random integer which is evenly distributed within the range [0,n].If the average processing time is T(n), what is the value of T(6)?
//Hint: Calucate the number of time random is coming.
int function(int n)
{
    int i;
    if (n <= 0)
    {
        return 0;
    }
    else
    {
        i = random(n - 1);
        printf("%d\n",i);
        return function(i) + function(n - 1 -i);
    }
}

int main()
{
    function(6);
    return 0;
}

