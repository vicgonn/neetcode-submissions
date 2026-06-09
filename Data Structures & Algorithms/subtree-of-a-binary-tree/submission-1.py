# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution:

    res = None

    def dfs(self, root):

        if root is None or self.res:
            return

        # print(root.val)

        self.res = self.sameTree(root, subRoot)
        self.dfs(root.left)
        self.dfs(root.right)

    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        self.dfs(root)
        return self.res
        # return False

    def sameTree(self, p, q):

        if not p and not q:
            return True

        if (not p and q) or (not q and p):
            return False

        if p.val != q.val:
            return False

        return self.sameTree(p.left, q.left) and self.sameTree(p.right, q.right)
        
