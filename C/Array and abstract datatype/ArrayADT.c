#include <stdio.h>
#include <stdlib.h>

struct myArray
{
    int total_size;
    int used_size;
    int *ptr;
};

// Contruction in c
void createArray(struct myArray *a, int tsize, int usize)
{

    /* //Also possible
    (*a).total_size = tsize; // Dereferencing
    (*a).used_size = usize;
    (*a).ptr = (int *)malloc(tsize * sizeof(int));
    */

    a->total_size = tsize; // Dereferencing
    a->used_size = usize;
    a->ptr = (int *)malloc(tsize * sizeof(int));
}

void show(struct myArray *a)
{
    for (int i = 0; i < a->used_size; i++)
    {
        printf("%d \n", (*a).ptr[i]); // (a->ptr)[i] is also same
    }
}

void setValue(struct myArray *a)
{
    for (int i = 0; i < (*a).used_size; i++)
    {
        int value;
        printf("\nEnter the element value for %d: ", i);
        scanf("%d", &value);
        (a->ptr)[i] = value;
    }
}

int main()
{
    struct myArray marks;
    createArray(&marks, 10, 2);
    setValue(&marks);//Setting the values
    show(&marks);//Showing the values
    return 0;
}