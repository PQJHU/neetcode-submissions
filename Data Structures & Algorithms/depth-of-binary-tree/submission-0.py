# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = [0]

        def find_max_depth(root: Optional[TreeNode], depth: int):
            if root is None:
                max_depth[0] = max(max_depth[0], depth)
                return
            # depth += 1
            find_max_depth(root.left, depth+1)
            find_max_depth(root.right, depth+1)
            # depth -= 1

        find_max_depth(root, 0)

        return max_depth[0]
        