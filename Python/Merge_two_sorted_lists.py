class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def mergeTwoLists(list1,list2):
    new_list = []
    for i in list1:
        new_list.append(i.val)
    for j in list2:
        new_list.append(j.val)

    new_list.sort()
    return new_list


list1_val= [1,2,4]
list2_val= [1,3,4]

list1 = ListNode()
current = list1
for val in list1_val:
    current.next = ListNode(val=val)
    current = current.next
list1 = list1.next

list2= ListNode()
current = list2
for val in list2_val:
    current.next = ListNode(val=val)
    current = current.next
list2 = list2.next

print(list1)
print(list2)

print(mergeTwoLists([1,2,4],[1,3,4]))