class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class UniqueBinarySearchTreesII(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []
        else:
            return self.generateTreesHelper(1, n)
    
    def generateTreesHelper(self, start, end):
        all_trees = []
        if start > end:
            all_trees.append(None)
            return all_trees
 
        for i in range(start, end + 1):
            # Generate all left and right subtrees
            left_trees = self.generateTreesHelper(start, i - 1)
            right_trees = self.generateTreesHelper(i + 1, end)
            
            # Combine left and right subtrees with the current node
            for left in left_trees:
                for right in right_trees:
                    current_tree = TreeNode(i)
                    current_tree.left = left
                    current_tree.right = right
                    all_trees.append(current_tree)
        
        return all_trees        