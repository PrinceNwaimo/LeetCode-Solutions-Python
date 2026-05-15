class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
import sys
class ValidateBinarySearchTree(object):
    def __init__(self):
        self.lastPrinted = -sys.maxsize - 1
    def isValidBST(self, root):
        if root == None:
            return True
        if self.isValidBST(root.left) == False:
            return False
        data = root.value
        if data <= self.lastPrinted:
            return False
        self.lastPrinted = data
        if self.isValidBST(root.right) == False:
            return False
        return True
           