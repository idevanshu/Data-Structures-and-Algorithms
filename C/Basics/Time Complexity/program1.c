#include <stdio.h>
//Calculate the time complexity of fucn1.
void func1(int array[], int length){
    //Intializing - first part be k1
    int sum = 0;
    int product = 1;

    //Calucating the sum - second part be k2
    for (int i = 0; i < length; i++)
    {
        sum += array[i];
    }

    //Calucating the mutiplication - third part be k3
    for (int i = 0; i < length; i++)
    {
        product *= array[i];
    }
    /*
    Total time complexity will be:
    Tn = k1 + k2n + k3n //hence k1 is not a dominatant term it can be neglected.
        = k2n + k3n
        = (k2+k3)n
        = k4n //which is big O n
        = O(n)//Here, n is length
        = 0(length)
    */
}

int main(){
    int arr[] = {1,2,3,4,5};
    func1(arr,5);
    return 0;
}