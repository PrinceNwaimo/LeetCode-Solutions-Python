class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class InorderSuccessorInBST(object):
    # @param {TreeNode} root
    # @param {TreeNode} p
    # @return {TreeNode}
    def inorderSuccessor(self, root, p):
        """
        :type root: TreeNode
        :type p: TreeNode
        :rtype: TreeNode
        """
        successor = None
        # Use 'value' attribute from TreeNode
        while root is not None and root.value != p.value:
            if root.value > p.value:
                successor = root
                root = root.left
            else:
                root = root.right
        # If node has right subtree, successor is the leftmost node there
        if root is not None and root.right is not None:
            node = root.right
            while node.left is not None:
                node = node.left
            return node
        return successor
    
    