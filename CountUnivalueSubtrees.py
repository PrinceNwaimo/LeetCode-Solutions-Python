# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CountUnivalueSubtrees(object):
    def __init__(self):
        self.__count = 0
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
    def countUnivalSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.count_univalue_subtrees(root)
        return self.__count
    def count_univalue_subtrees(self, root):
        if root == None:
            return True
        if root.left == None and root.right == None:
            self.__count += 1
            return True
        left = self.count_univalue_subtrees(root.left)
        right = self.count_univalue_subtrees(root.right)
        if (left and right) and (root.left == None or root.left.val == root.val) and (root.right == None or root.right.val == root.val):             
            self.__count += 1
            return True         
        else:             
            return False