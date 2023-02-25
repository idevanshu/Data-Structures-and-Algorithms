class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeKLists(lists):
    head = tmp = ListNode()
    arr = []

    for l in lists:
        while l != None:
            arr.append(l.val)
            l = l.next

    for val in sorted(arr):
        tmp.next = ListNode()
        tmp = tmp.next
        tmp.val = val

    return head.next

print(mergeKLists([[1,4,5],[1,3,4],[2,6]]))