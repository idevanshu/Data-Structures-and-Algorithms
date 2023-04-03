#include <stdio.h>
#include <stdlib.h>

struct stack
{
    int size;
    int top;
    int *arr;
};

int isEmpty(struct stack *ptr)
{
    if (ptr->top == -1)
    {
        return 1;
    }
    return 0;
};

int isFull(struct stack *ptr)
{
    if (ptr->top == ptr->size - 1)
    {
        return 1;
    }
    return 0;
};

int main()
{
    // struct stack s;
    // s.size = 80;
    // s.top = -1;
    // s.arr = (int *)malloc(s.size * sizeof(int));

    struct stack *s;
    s->size = 6;
    s->top = -1;
    s->arr = (int *)malloc(s->size * sizeof(int));

    //pushing an element manullay
    s->arr[0] = 7;
	s->top++;
	s->arr[1] = 5;
	s->top++;
	s->arr[2] = 8;
	s->top++;
	s->arr[3] = 9;
	s->top++;
	s->arr[4] = 10;
	s->top++;
	s->arr[5] = 15;
	s->top++;

    //Checking is stack is empty
    if(isEmpty(s)){
        printf("The stack is empty. \n");
    }else{
        printf("The stack is not empty. \n");
    }

    //Checking is stack is full
    if(isFull(s)){
        printf("The stack is Full. \n");
    }else{
        printf("The stack is not Full. \n");
    }

    return 0;
}