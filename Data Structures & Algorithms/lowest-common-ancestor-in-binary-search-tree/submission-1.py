# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    res = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        self.dfs(root)

        return self.res
        
    
    def dfs(self, root):

        if root is None or self.res:
            return
        
        # print(root.val)
        lower = None
        higher = None
        if p.val <= q.val:
            lower = p
            higher = q
        else:
            lower = q
            higher = p

        if root.val >= lower.val and root.val <= higher.val:
            self.res = root
        self.dfs(root.left)
        self.dfs(root.right)


