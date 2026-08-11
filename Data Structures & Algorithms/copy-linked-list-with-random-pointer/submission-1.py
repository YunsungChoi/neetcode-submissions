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

        if not head:
            return None

        curr = head
        while curr:
            tmp = curr.next
            curr.next = Node(curr.val)
            curr.next.next = tmp
            curr = tmp
        
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next 
            curr = curr.next.next

        curr = head
        result = head.next
        while curr:
            copy = curr.next
            curr.next = copy.next
            copy.next = curr.next.next if curr.next else None
            curr = curr.next            

        return result
        
        

            
        