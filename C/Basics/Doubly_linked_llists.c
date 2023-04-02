#include <stdio.h>
#include <stdlib.h>

struct Node
{
    struct Node *prev;
    int data;
    struct Node *next;
};

void normalTraversel(struct Node* head){
    printf("Normal Traversel \n");
    struct Node * ptr = head;
    while(ptr!=NULL){
        printf(" %d \n",ptr->data);
        ptr = ptr->next;
    }
}

void reverseTraversel(struct Node* lastElement){
    printf("Reverse Traversal \n");
    struct Node *ptr = lastElement;
    while (ptr!=NULL)
    {
        printf(" %d \n",ptr->data);
        ptr = ptr->prev;
    }
}

int main()
{
    struct Node * head, *first, *second, *third, *fourth;
    head = (struct Node*)malloc(sizeof(struct Node));
    first = (struct Node*)malloc(sizeof(struct Node));
    second = (struct Node*)malloc(sizeof(struct Node));
    third = (struct Node*)malloc(sizeof(struct Node));
    fourth = (struct Node*)malloc(sizeof(struct Node));
    
    head->prev=NULL;
    head->data = 1;
    head->next= first;

    first->prev = head;
    first->data = 2;
    first->next = second;

    second->prev = first;
    second->data = 3;
    second->next = third;

    third->prev = second;
    third->data = 4;
    third->next = fourth;

    fourth->prev = third;
    fourth->data = 5;
    fourth->next = NULL;

    normalTraversel(head);
    reverseTraversel(fourth);

    return 0;
}