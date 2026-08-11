# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        while root:
            if p.val < root.val and q.val < root.val:
                root = root.left          # 둘 다 왼쪽 → 왼쪽으로
            elif p.val > root.val and q.val > root.val:
                root = root.right         # 둘 다 오른쪽 → 오른쪽으로
            else:
                return root               # 갈라짐 (또는 하나가 나 자신) = LCA