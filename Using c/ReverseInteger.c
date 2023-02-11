#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>
#include <limits.h>
#include <limits.h>
int reverse_digits(int x) {
    long long reversed_x = 0;
    if (x == 0) {
        return 0;
    } else if (x == INT_MIN) {
        return 0;
    }
    int sign = (x > 0) - (x < 0);
    x = abs(x);
    while (x > 0) {
        reversed_x = (reversed_x * 10) + (x % 10);
        x /= 10;
    }
    if (reversed_x > INT_MAX) {
        return 0;
    } else {
        return sign * reversed_x;
    }
}

int main(int argc, char const *argv[])
{
    printf("%d",reverse_digits(-123));
    
    return 0;
}