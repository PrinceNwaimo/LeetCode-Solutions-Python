class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class InvertBinaryTree(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        else:
             stack = []
             stack.append(root)
        while stack != []:
            curr_node = stack.pop()
        if curr_node.left != None  or curr_node.right != None: 
            temp = curr_node.left
            curr_node.left = curr_node.right
            curr_node.right = temp
        if curr_node.left != None:
            stack.append(curr_node.left)
        if curr_node.right != None:
            stack.append(curr_node.right)
        return root
         