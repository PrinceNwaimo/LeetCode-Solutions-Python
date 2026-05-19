class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class FlattenBinaryTreeToLinkedList(object):
    def flatten(self, root):
        """ :type root: TreeNode :rtype: void Do not return anything, modify root in-place instead. """
        if root is None:
            return root
        stack = []
        current = root
        while ((stack is not []) or (current is not None)):
            if current.right is not None:
                stack.append(current.right)
            if current.left is not None:
                current.right = current.left
                current.left = None
            else:
                if stack is not []:
                    temp = stack.pop()
                    current.right = temp
            current = current.right
            
            