#剑指 Offer 18. 删除链表的节点
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head.val == val:
            return head.next
        p = head
        pre = p
        while p:
            if p.val == val:
                pre.next = p.next
                return head
            else:
                pre = p
                p = p.next
        return head
