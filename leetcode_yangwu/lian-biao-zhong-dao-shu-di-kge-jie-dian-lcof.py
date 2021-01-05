#剑指 Offer 22. 链表中倒数第k个节点
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getKthFromEnd(self, head: ListNode, k: int) -> ListNode:
        n = 0
        p = head
        while p:
            n += 1
            p = p.next
        if n < k:
            return None
        i = 0
        while head:
            i += 1
            if i == n - k + 1:
                return head
            head = head.next
        return head
