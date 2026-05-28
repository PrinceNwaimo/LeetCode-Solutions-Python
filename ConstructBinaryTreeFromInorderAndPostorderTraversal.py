class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class ConstructBinaryTreeFromInorderAndPostorderTraversal(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        return self.create_tree(inorder, 0, len(inorder) -1 , postorder, 0, len(postorder) - 1)
    def search_divindex(self, inorder, low_inorder, high_inorder, val):
        for i in range(low_inorder, high_inorder+1):
            if inorder[i] == val:
                return i
        return -1
    def create_tree(self, inorder, low_inorder, high_inorder, postorder, low_postorder, high_postorder):
        if (low_inorder > high_inorder) or (low_postorder > high_postorder):
            return None  
        root = TreeNode(postorder[high_postorder])
        size_left_subtree = div_index - low_inorder
        size_right_subtree = high_inorder - div_index
        div_index = self.search_divindex(inorder, low_inorder, high_inorder, root.val)
        root.right = self.create_tree(inorder, div_index + 1, high_inorder, postorder, high_postorder - size_right_subtree, high_postorder - 1)
        root.left = self.create_tree(inorder, low_inorder, div_index - 1,postorder,high_postorder - size_right_subtree - size_left_subtree, high_postorder - size_right_subtree - 1)
        return root    