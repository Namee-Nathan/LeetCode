# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right
class Solution(object):
    def addOneRow(self, root, val, depth):
        """
        :type root: TreeNode
        :type val: int
        :type depth: int
        :rtype: TreeNode
        """
        if depth == 1:
            return TreeNode(val, root, None)

        def dfs(node, level):
            if not node:
                return
            level -= 1
            if level == 1:
                node.left = TreeNode(val, node.left, None)
                node.right = TreeNode(val, None, node.right)
            else:
                dfs(node.left, level)
                dfs(node.right, level)

        dfs(root, depth)

        return root
