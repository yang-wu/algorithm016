#面试题 02.07. 链表相交
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pa = headA
        pb = headB
        while pa != pb:  #如果相交，两个链表肯定步调会相遇
            pa = pa.next if pa else headB  #先遍历链表A，然后遍历B
            pb = pb.next if pb else headA  #先遍历链表B，然后遍历A
        return pa
