#include <stdio.h>
#include <stdlib.h>

struct Node
{
    int data;
    struct Node *next;
};

void linkedListTravesal(struct Node *ptr)
{
    while (ptr != NULL)
    {
        printf("Element: %d \n", ptr->data);
        ptr = ptr->next;
    }
}

// Deleting the first element from the linked list.
struct Node *deleteFirst(struct Node *head)
{
    struct Node *ptr = head;
    head = head->next;
    free(ptr);
    return head;
}

// Deleting the element at a given index
struct Node *deleteAtIndex(struct Node *head, int index)
{
    struct Node *ptr = head;
    struct Node *q = head->next;
    // Assuming that we want to do deletion from index 1.
    for (int i = 0; i < index - 1; i++)
    {
        ptr = ptr->next;
        q = q->next;
    }
    ptr->next = q->next;
    free(q);
    return head;
}

// Deleting the last element
struct Node *deleteLast(struct Node *head)
{
    struct Node *p = head;
    struct Node *q = head->next;
    while (q->next != NULL)
    {
        p = p->next;
        q = q->next;
    }
    p->next = NULL;
    free(q);
    return head;
}

// Deleting the element with a given value
struct Node *deleteAtValue(struct Node *head, int value)
{
    struct Node *p = head;
    struct Node *q = head->next;

    while (q->data != value && q->next != NULL)
    {
        p = p->next;
        q = q->next;
    }
    if (q->data == value)
    {
        p->next = q->next;
        free(q);
    }
    return head;
}

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
    printf("Before \n");
    linkedListTravesal(head);
    // head = deleteFirst(head);//Deleting first element
    // head = deleteAtIndex(head,1);//Deleting second element
    // head = deleteLast(head);//Deleting the last element
    head = deleteAtValue(head, 11); // Deleting the element by giving it's value
    printf("After \n");
    linkedListTravesal(head);
    return 0;
}