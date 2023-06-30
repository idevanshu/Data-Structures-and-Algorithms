class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    if not head or not head.next:
        return head

    current = head
    while current.next:
        if current.val == current.next.val:
            current.next = current.next.next
        else:
            current = current.next
        
    return head.val

# Create the nodes
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(2)
node4 = ListNode(3)
node5 = ListNode(3)

# Connect the nodes
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Assign the head of the linked list
head = node1

print(deleteDuplicates(head))