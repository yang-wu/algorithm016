#剑指 Offer 24. 反转链表
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p1 = head
        p2 = head.next
        p1.next = None
        while p2:
            tmp = p2.next
            p2.next = p1
            p1 = p2
            p2 = tmp
        return p1
