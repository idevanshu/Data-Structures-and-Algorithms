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
// Index insertion
/*
    Basic insertion
    contains array, size of it, new element to insert, capacity,index(position).
*/
int indInsertion(int arr[], int size, int element, int capacity, int index)
{
    if (size >= capacity)
    {
        return 0;
    }

    for (int i = size - 1; i >= index; i--)
    {
        arr[i + 1] = arr[i];
    }
    arr[index] = element;
    return 1;
}

int main()
{
    int arr[10] = {1, 27, 31, 24, 15, 6};
    int size = 6, element = 21, index = 3;
    display(arr, size);

    if (indInsertion(arr, size, element, 100, index))
    {
        size += 1;
        display(arr, size);
    }
    else
    {
        printf("Insertion failed!!!");
    }
    return 0;
}