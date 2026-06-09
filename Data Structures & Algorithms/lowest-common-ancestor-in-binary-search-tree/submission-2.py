# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:

    res = None

    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        # print(root.val)
        lower = None
        higher = None
        if p.val <= q.val:
            lower = p
            higher = q
        else:
            lower = q
            higher = p

        self.dfs(root, lower, higher)

        return self.res
        
    
    def dfs(self, root, lower, higher):

        if root is None or self.res:
            return
        
        if root.val >= lower.val and root.val <= higher.val:
            self.res = root
        self.dfs(root.left, lower, higher)
        self.dfs(root.right, lower, higher)


