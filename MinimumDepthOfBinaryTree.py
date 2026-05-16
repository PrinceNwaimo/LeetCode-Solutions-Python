import sys

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class MinimumDepthOfBinaryTree(object):
    def minDepth(self, root):
        """Return the minimum depth of the binary tree.

        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        # If one child is None, must consider the depth of the other child
        if root.left is None and root.right is None:
            return 1
        if root.left != None:
           left = self.minDepth(root.left)
        else:
            left = sys.maxsize
        if root.right != None:
            right = self.minDepth(root.right)
        else:
            right = sys.maxsize
        return min(left, right) + 1
        