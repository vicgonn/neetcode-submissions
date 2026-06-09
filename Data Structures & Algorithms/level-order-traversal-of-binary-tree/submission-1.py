# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        # exit early if root is None
        if not root:
            return []

        # bfs
        queue = deque()
        queue.append(root)

        # print(queue)
        res = []

        while queue:
            level_list = []
            level_len = len(queue)

            for _ in range(level_len):

                tempNode = queue.popleft()
                level_list.append(tempNode.val)

                if tempNode.left:
                    queue.append(tempNode.left)
                if tempNode.right:
                    queue.append(tempNode.right)
                
            res.append(level_list)
        
        return res

