class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class MaximumDepthOfBinaryTree(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            left_depth = self.maxDepth(root.left)
            right_depth = self.maxDepth(root.right)
            return max(left_depth, right_depth) + 1
        
                