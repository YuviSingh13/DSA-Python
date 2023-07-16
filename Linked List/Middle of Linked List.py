from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    '''
    # Function 1 Naive Approach
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        n = 0
        temp = head
        while temp:
            n += 1
            temp = temp.next
        temp = head
        for i in range(n // 2):
            temp = temp.next
        return temp
    '''
    # Function 2 Optimal Approach
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast, slow = head, head
        while fast != None and fast.next != None:
            slow = slow.next
            fast = fast.next.next
        return slow
