class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class ClosestBinarySearchTreeValue(object):
    def closestValue(self, root, target):
      """
      :type root: TreeNode
      :type target: float
      :rtype: int
    """
    min_diff = float('inf')
    closestValue = None
    
    def helper(self, root, target):
        if root is None:
            return
        
        diff = abs(root.val - target)
        if diff < self.min_diff:
            self.min_diff = diff
            self.closestValue = root.val
            
        if target < root.val:
            self.helper(root.left, target)
        else:
            self.helper(root.right, target)
        self.helper(root, target)
        return self.closestValue

    