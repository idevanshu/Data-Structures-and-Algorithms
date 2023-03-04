#include <stdio.h>
#include <stdlib.h>

// Linear Search
int linearSearch(int arr[], int size, int element)
{
    for (int i = 0; i < size; i++)
    {
        if (arr[i] == element)
        {
            return i;
        }
    }
    return 0;
}

// Binary Search
int binarySearch(int arr[], int size, int element)
{
    int mid, low = 0, high = size - 1;
    // Keep Searching until low <=> high
    while (low <= high)
    {
        mid = (low + high) / 2;
        if (arr[mid] == element)
        {
            return mid;
        }
        if (arr[mid] < element)
        {
            low = mid + 1;
        }
        else
        {
            high = mid - 1;
        }
    }
    return 0;
}
int main()
{
    int arr[] = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10};
    int size = sizeof(arr) / sizeof(int);
    int element = 8;

    // Using Linear Search
    int searchIndex = linearSearch(arr, size, element);
    printf("The element %d is in index %d. \n", element, searchIndex);

    // Using Binary Search
    int Searchindex = binarySearch(arr, size, element);
    printf("The element %d is in index %d. \n", element, Searchindex);

    return 0;
}