# class TreeNode:
#      def __init__(self, value):
#          self.value = value
#          self.left = None
#          self.right = None
         
class PreorderTraversal:
    # @param {TreeNode} root
    # @return {integer[]}
    def preorderTraversal(self, root):
        if root == None:
            return []
        else:
            preorderList = []
            stack = []
            stack.append(root)
            while (stack != []):
                node = stack.pop()
                preorderList.append(node.value)
                if node.right != None:
                    stack.append(node.right)
                if node.left != None:
                    stack.append(node.left)
            return preorderList
        
        