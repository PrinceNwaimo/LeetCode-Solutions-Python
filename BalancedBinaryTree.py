class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class BalancedBinaryTree:
    def isBalanced(self, root):
        if self.getHeight(root) == -1:
            return False
        else:
            return True
    def getHeight(self, root):    
        if root == None:
            return 0
        
        leftHeight = self.getHeight(root.left)
        if leftHeight == -1:
            return -1   
        
        rightHeight = self.getHeight(root.right)
        if rightHeight == -1:
            return -1
        
        heightDiff = abs(leftHeight - rightHeight)
        if heightDiff > 1:
            return -1
        else:
            return max(leftHeight, rightHeight) + 1
        
        