from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None or head.next is None or k == 0:
            return head

        cur = head
        list_len = 1
        while cur.next:
            cur = cur.next
            list_len += 1

        cur.next = head
        k = k % list_len
        k = list_len - k

        while k:
            cur = cur.next
            k -= 1
        head = cur.next
        cur.next = None

        return head