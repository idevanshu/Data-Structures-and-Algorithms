#include <stdio.h>
#include <stdlib.h>

struct stack
{
    int size;
    int top;
    int *arr;
};

int isFull(struct stack *ptr)
{
    if (ptr->top == ptr->size - 1)
    {
        return 1;
    }
    return 0;
};

int isEmpty(struct stack *ptr)
{
    if (ptr->top == -1)
    {
        return 1;
    }
    return 0;
};

int peek(struct stack *sp, int i)
{
    int arrayInd = sp->top - i + 1;
    if (arrayInd < 0)
    {
        printf("Not a valid postion for the stack");
        return -1;
    }
    return sp->arr[arrayInd];
};

void push(struct stack *ptr, int val)
{
    if (isFull(ptr))
    {
        printf("Stack OverFlow! Cannot push %d to the stack.\n", val);
    }
    else
    {
        ptr->top++;
        ptr->arr[ptr->top] = val;
    }
};

// Last in first out.
int pop(struct stack *ptr)
{
    if (isEmpty(ptr))
    {
        printf("Stack UnderFlow! Stack is Empty");
        return -1; // Assuming that -1 is not going to be present in my stack.
    }
    else
    {
        int val = ptr->arr[ptr->top];
        ptr->top--;
        return val;
    }
}

int main()
{
    struct stack *sp = (struct stack *)malloc(sizeof(struct stack));

    sp->size = 10;
    sp->top = -1; // Means nothing is at the top.
    sp->arr = (int *)malloc(sp->size * sizeof(int));

    push(sp, 1);
    push(sp, 2);
    push(sp, 3);
    push(sp, 4);
    push(sp, 5);
    push(sp, 6);
    push(sp, 7);
    push(sp, 8);
    push(sp, 9);
    push(sp, 10);

    printf("Popped %d from the stack.\n", pop(sp));

    // Printing values from the stack.
    for (int j = 1; j < sp->top + 1; j++)
    {
        printf("The Value at postion %d is %d\n", j, peek(sp, j));
    }

    return 0;
}