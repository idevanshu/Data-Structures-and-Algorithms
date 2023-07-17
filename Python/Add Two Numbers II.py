class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    num1, num2 = 0, 0

    while l1:
        num1 = num1 * 10 + l1.val
        l1 = l1.next

    while l2:
        num2 = num2 * 10 + l2.val
        l2 = l2.next

    sums = num1 + num2

    currentHead = head = ListNode(0)

    if sums == 0:
        return head

    while sums > 0:
        head.next = ListNode(sums % 10)
        head = head.next
        sums //= 10

    previous = None
    head = currentHead.next
    while head:
        nxt = head.next
        head.next = previous
        previous = head
        head = nxt

    return previous


l1_node3 = ListNode(3)
l1_node4 = ListNode(4, l1_node3)
l1_node2 = ListNode(2, l1_node4)

l2_node4 = ListNode(4)
l2_node6 = ListNode(6, l2_node4)
l2_node5 = ListNode(5, l2_node6)

result_head = addTwoNumbers(l1_node2, l2_node5)
print(result_head.val)
