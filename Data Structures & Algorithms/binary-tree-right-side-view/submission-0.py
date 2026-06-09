# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # exit in case of no root

        if not root:
            return []

        # do a bfs, only add the last values from the range
        res = []
        queue = deque()
        queue.append(root)

        while queue:
            level_list = []

            level_len = len(queue)
            for i in range(level_len):

                tempNode = queue.popleft()

                # only care for right most value at the level
                if i == (level_len - 1):
                    res.append(tempNode.val)

                if tempNode.left:
                    queue.append(tempNode.left)

                if tempNode.right:
                    queue.append(tempNode.right)

        return res                 


