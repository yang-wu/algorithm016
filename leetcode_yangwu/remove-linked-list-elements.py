#203. 移除链表元素
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head:
            if val == head.val:
                head = head.next
            else:
                break
        if not head:
            return head
        p1 = head
        p2 = head.next
        while p2:
            if val == p2.val:
                p1.next = p2.next
                p2 = p1.next
            else:
                p1 = p2
                p2 = p2.next
        return head

