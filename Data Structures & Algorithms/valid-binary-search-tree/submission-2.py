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



#### alternative

# class Solution:
#     def isValidBST(self, root: Optional[TreeNode]) -> bool:
#         self.prev = float('-inf')
#         return self.inOrder(root)

#     def inOrder(self, root):
#         if root is None:
#             return True  # An empty tree/leaf boundary is inherently valid

#         # 1. Ask the left child: "Are you a valid BST?"
#         if not self.inOrder(root.left):
#             return False  # If left says False, I immediately return False!

#         # 2. Check the current node (In-order stage)
#         if root.val <= self.prev:
#             return False  # If I break the rule, I return False!
#         self.prev = root.val  # Update prev for the next guy
        # # 3. Ask the right child: "Are you a valid BST?"
        # if not self.inOrder(root.right):
        #     return False  # If right says False, I return False!
                    
        # # 4. If everything passed (Left, Me, and Right), then I am valid!
        #     return True






