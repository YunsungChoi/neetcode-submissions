"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        oldToNew = {} #hash map
        def copyNode(node):
            if node == None:
                return None

            if node in oldToNew:
                return oldToNew[node]
            
            copiedNode = Node(node.val) #create
            oldToNew[node] = copiedNode #save

            for nei in node.neighbors:
                copiedNode.neighbors.append(copyNode(nei))
            return copiedNode
    
        return copyNode(node)

        
        