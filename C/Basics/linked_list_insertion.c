#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node * next;
};

void linkedListTravesal(struct Node *ptr)
{
    while (ptr != NULL)
    {
        printf("Element: %d \n", ptr->data);
        ptr = ptr->next;
    }
}

struct Node * insertAtFirst(struct Node * head, int data)
{
    struct Node * ptr = (struct Node *) malloc(sizeof(struct Node));
    ptr->next = head;
    ptr->data = data;
    return ptr;
};

struct Node * insertAtEnd(struct Node * head,int data){
    struct Node * ptr = (struct Node *) malloc(sizeof(struct Node));
    ptr->data = data;
    struct Node * p = head;

    while (p->next!=NULL)
    {
        p = p->next;
    }
    p->next = ptr;
    ptr->next = NULL;
    return head;
}

struct Node * insertAfterNode(struct Node *head,struct Node * previousNode,int data){
    struct Node * ptr = (struct Node *) malloc(sizeof(struct Node));
    ptr->data = data;

    ptr->next = previousNode->next;
    previousNode->next = ptr;

    return head;
}

struct Node * insertAtIndex(struct Node *head,int data, int index)
{
    struct Node * ptr = (struct Node *) malloc(sizeof(struct Node));
    struct Node * p = head;
    int i = 0;

    while (i!=index-1)
    {
        p= p->next;
        i++;
    }

    ptr->data = data;
    ptr->next = p->next;
    p->next = ptr;
    return ptr;
};


int main()
{
    struct Node *head;
    struct Node *second;
    struct Node *third;

    // Allocate memory for nodes in the linked list in Heap
    head = (struct Node *)malloc(sizeof(struct Node));
    second = (struct Node *)malloc(sizeof(struct Node));
    third = (struct Node *)malloc(sizeof(struct Node));

    // Link first and second nodes
    head->data = 7;
    head->next = second;

    // Link second and third node
    second->data = 11;
    second->next = third;

    // Terminating
    third->data = 54;
    third->next = NULL;
    printf("\n");
    linkedListTravesal(head);
    head = insertAtFirst(head,56);
    printf("\n");
    linkedListTravesal(head);
    head = insertAtIndex(head,78,1);
    printf("\n");
    linkedListTravesal(head);
    head = insertAtEnd(head,89);
    printf("\n"); 
    linkedListTravesal(head);
    printf("\n");
    head = insertAfterNode(head,second,37);
    linkedListTravesal(head);

    return 0;
}
