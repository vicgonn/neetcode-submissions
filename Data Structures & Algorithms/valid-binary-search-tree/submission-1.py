# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        self.prev = float("-inf")

        self.res = True


        self.inOrder(root)

        return self.res


    def inOrder(self, root):
        if root is None or not self.res:
            return

        self.inOrder(root.left)

        print(root.val)
        print(self.prev)
        print("####")

        if root.val <= self.prev:
            self.res = False
        
        self.prev = root.val

        self.inOrder(root.right)










