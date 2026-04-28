class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None
        
class InorderTraversal:
    def inorderTraversal(self, root):
        if root == None:
            return []
        else:
            result = []
            stack = []
            node = root
            while stack or node:
                if node:
                    stack.append(node)
                    node = node.left
                else:
                    node = stack.pop()
                    result.append(node.value)
                    node = node.right
            return result
        