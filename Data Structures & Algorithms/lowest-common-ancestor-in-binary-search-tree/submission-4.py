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
        # BST: (left < node < right)
        # Since it is a BST it is in the order that root is greater or equal than left and less or equal than right
        
        # find which is lower value p or q


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

        # basic dfs return condition to pop from stack or if result has been found
        if root is None or self.res:
            return
        
        # following BST if the root is >= to the lower and also the root is less than the higher value,
        # we have found our lowest common ancestor solution, so do a self.res assigment so dfs can stop.
        # Remember: if p.val <= root.val <= q.val (or vice versa), the current node is the LCA.
        if root.val >= lower.val and root.val <= higher.val:
            self.res = root
        self.dfs(root.left, lower, higher)
        self.dfs(root.right, lower, higher)


