class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTreeMaxPathSum(object):
    def __init__(self):
        self.max_sum = -float('inf')
        
    def maxPathSum(self, root):
        self.findMax(root)
        return self.max_sum
    
    def findMax(self, root):
        if root == None:
            return 0
        left = max(0, self.findMax(root.left))
        right = max(0, self.findMax(root.right))
        self.max_sum = max(self.max_sum, left + right + root.value)
        return max(left, right) + root.value
        
        