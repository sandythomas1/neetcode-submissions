"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        copy = {None: None}

        curr = head
        while curr:
            curr_copy = Node(curr.val)
            copy[curr] = curr_copy
            curr = curr.next
        
        curr = head
        while curr:
            curr_copy = copy[curr]
            curr_copy.next = copy[curr.next]
            curr_copy.random = copy[curr.random]
            curr = curr.next

        return copy[head]
        