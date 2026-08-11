# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.res = 0
        
        def findNodes(maxVal, node):
            if not node:
                return
            if node.val >= maxVal:
                self.res +=1
            findNodes(max(maxVal, node.val), node.left)
            findNodes(max(maxVal, node.val), node.right)
        
        findNodes(root.val, root)

        return self.res
                
            
            
        
        
        