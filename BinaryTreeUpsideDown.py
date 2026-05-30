# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class BinaryTreeUpsideDown(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        pole = root
        parent = None  
        parent_right = None
        while pole:
            left = pole.left
            pole.left = parent_right
            parent_right = pole.right
            pole.right = parent
            parent = pole
            pole = left
        return parent
    