class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
 
class Kth_SmallestElement_BST(object):
    def kthSmallest(self, root, k):
        """ :type root: TreeNode :type k: int :rtype: int """
        if root == None:
            return None
        else:
            stack = []
            current = root
            count = 0
            
            while stack != [] or current != None:
                if current != None:
                    stack.append(current)
                    current = current.left
                else:
                    current = stack.pop()
                    count += 1
                    if count == k:
                        return current.value
                    current = current.right
                return None
            
class Kth_SmallestElement_BST2(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        stack = []*k
        while True:
            while root:
                stack.append(root)
                root = root.left 
                root = stack.pop()
            if k == 1:
                return root.val
            else:
                k -= 1
                root = root.right           
               