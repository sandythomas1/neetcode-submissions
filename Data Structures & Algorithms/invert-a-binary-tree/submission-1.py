# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # flip left and right children until end of tree
        # return empty on empty list
        # bfs or dfs approach to recursivly swap children level by level(dfs is probably better)


        if not root:
            return None

        stack = [root]
        while stack:
            curr = stack.pop()
            curr.left, curr.right = curr.right, curr.left

            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        return root

        