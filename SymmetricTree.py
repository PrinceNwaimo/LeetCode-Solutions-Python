class treeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class SymmetricTree(object):
    def isSymmetric(self, root):
        """ :type root: treeNode
            :rtype: bool
        """
        if root == None:
            return True
        else:
            return self.isMirror(root.left, root.right)
    def isMirror(self, root1, root2):  
        if root1 == None and root2 == None:
            return True
        elif root1 == None or root2 == None:
            return False
        else:
            if root1.value != root2.value:
                return self.isMirror(root1.left, root2.right) and self.isMirror(root1.right, root2.left)
            else:
                return False
            
            
        