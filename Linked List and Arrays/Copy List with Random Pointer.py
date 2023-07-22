from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        '''oldToCopy = {None : None}

        cur = head

        while cur:
            copy_ = Node(cur.val)
            oldToCopy[cur] = copy_
            cur = cur.next

        cur = head
        while cur:
            copy_ = oldToCopy[cur]
            copy_.next = oldToCopy[cur.next]
            copy_.random = oldToCopy[cur.random]
            cur = cur.next

        return oldToCopy[head]'''

        itr = head

        while itr is not None:
            front = itr.next
            copy = Node(itr.val)
            itr.next = copy
            copy.next = front
            itr = front

        itr = head
        while itr is not None:
            if itr.random is not None:
                itr.next.random = itr.random.next
            itr = itr.next.next

        itr = head
        pseudoNode = Node(0)
        copy = pseudoNode
        while itr is not None:
            front = itr.next.next
            copy.next = itr.next
            itr.next = front
            copy = copy.next
            itr = itr.next

        return pseudoNode.next