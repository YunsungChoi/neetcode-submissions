# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def calSum(root):
            if not root:
                return 0
            else:
                l = calSum(root.left)
                r = calSum(root.right)
                self.res = max(self.res, l + r)
                return 1 + max(l, r)
        calSum(root)
        return self.res
            

        