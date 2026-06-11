# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        self.counter = 0
        # self.current_max = float('-inf')

        self.dfs(root)
        return self.counter

    def dfs(self, root, current_max = float('-inf')):

        if not root:
            return

        print(current_max)
        if current_max <= root.val:
            # print(root.val)
            self.counter += 1
            current_max = root.val

        self.dfs(root.left, current_max)
        self.dfs(root.right, current_max)
        