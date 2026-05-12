class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

        
class PathSum(object):
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if root == None:
            return False
        else:
            current = root
            stack  = []
            stack.append(current)
            stack.append(current.value)
            
            while stack != []:
                PathSum = stack.pop()
                current = stack.pop()
                if not current.left and not current.right and PathSum == sum:
                    return True 
                if current.right:
                    rightpathsum = PathSum + current.right.value
                    stack.append(current.right)
                    stack.append(rightpathsum)
                if current.left:
                    leftpathsum = PathSum + current.left.value
                    stack.append(current.left)
                    stack.append(leftpathsum)   
        return False
    
    
    
        
        