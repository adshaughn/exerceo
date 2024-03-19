# https://leetcode.com/problems/merge-two-sorted-lists/


# Definition for singly-linked list provided by Leetcode
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:

        dummy = ListNode()
        current = dummy

        while l1 and l2:
            if l1.val < l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        # Append remaining elements if any
        if l1:
            current.next = l1
        elif l2:
            current.next = l2

        return dummy.next


# Example usage:
# Create example linked lists
list1 = ListNode(1)
list1.next = ListNode(3)
list1.next.next = ListNode(5)

list2 = ListNode(2)
list2.next = ListNode(4)
list2.next.next = ListNode(6)

# Merge the two lists
merged_list = mergeTwoLists(list1, list2)

# Print the merged list
while merged_list:
    print(merged_list.val, end=" -> ")
    merged_list = merged_list.next
