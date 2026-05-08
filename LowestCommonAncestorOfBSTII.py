class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class LowestCommonAncestorOfBSTII:
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        if root == p or root == q:
            return root
        left_lca = self.lowestCommonAncestor(root.left, p, q)
        right_lca = self.lowestCommonAncestor(root.right, p, q)
        if left_lca != None and right_lca != None:
            return root
        if left_lca == None:
            return right_lca
        else:
            return left_lca
        