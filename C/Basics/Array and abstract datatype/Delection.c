#include <stdio.h>
#include <stdlib.h>

void display(int arr[], int n)
{
    // Traversal
    for (int i = 0; i < n; i++)
    {
        printf("%d ", arr[i]);
    }
    printf("\n");
}
// Deleting an element from an array
/*
    Basic Delection
    contains array, size, index(position).
*/
void indDelection(int arr[], int size, int index)
{
    for (int i = index; i < size; i++)
    {
        arr[i] = arr[i + 1];
    }
}

int main()
{
    int arr[] = {1, 27,23, 31, 24, 15, 6};
    int size = sizeof(arr)/sizeof(arr[0]), index = 3;
    display(arr, size);
    indDelection(arr, size, index);
    size -= 1;
    display(arr, size);
    return 0;
}