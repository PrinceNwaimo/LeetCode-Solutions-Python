class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class BinaryTreePaths(object):
    def binaryTreePaths(self, root):
        """ :type root: TreeNode :rtype: List[str] """
        if not root:
            return []
        else:
            paths = []
            current = root
            solution = []
            solution.append(str(current.value))
            solution.append(current)
            
            while solution != []:
                path = solution.pop()
                node = solution.pop()
                if node.left == None and node.right == None:
                    paths.append(path)
                if node.right:
                    rightStr = path + "->" + str(node.right.value)
                    solution.append(rightStr)
                    solution.append(node.right)
                if node.left:
                    leftStr = path + "->" + str(node.left.value)
                    solution.append(leftStr)
                    solution.append(node.left)
            return paths
                