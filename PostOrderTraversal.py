class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class PostOrderTraversal:
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == None:
            return []
        else:
            stack = []
            out_stack = []
            stack.append(root)
            
            while stack != []:
                current = stack.pop()
                out_stack.append(current.value)
                if current.left != None:
                    stack.append(current.left)
                if current.right != None:
                    stack.append(current.right)
            return out_stack[::-1]
        
        
                   