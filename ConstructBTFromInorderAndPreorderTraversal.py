class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class ConstructBTFromInorderAndPreorderTraversal(object):
    def buildTree(self, preorder, inorder):
        """ :type preorder: List[int] :type inorder: List[int] :rtype: TreeNode """
        if len(inorder) == 1:
            return TreeNode(inorder[0])
        return self.create_tree(inorder,0,len(inorder)-1,preorder,0,len(preorder)-1)
    
    def search_divIndex(self, inorder, start, end, value):
        for i in range(start,end+1):
            if inorder[i] == value:
                return i
        return -1
    def create_tree(self, inorder, in_start, in_end, preorder, pre_start, pre_end):
        if in_start > in_end or pre_start > pre_end:
            return None
        root = TreeNode(preorder[pre_start])
        div_index = self.search_divIndex(inorder, in_start, in_end, preorder[pre_start])
        size_left = div_index - in_start
        size_right = in_end - div_index
        root.right = self.create_tree(inorder, div_index+1, in_end, preorder, pre_start+size_left+1, pre_end)
        root.left = self.create_tree(inorder, in_start, div_index-1, preorder, pre_start+1, pre_start+size_left)
        return root
    