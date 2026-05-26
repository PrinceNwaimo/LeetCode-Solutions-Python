class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class PathSum2(object):
    def pathSum(self, root, sum):
        """ :type root: TreeNode :type sum: int :rtype: List[List[int]] """
        if root == None:
            return []
        else:
            stack =[]
            paths = []
            
            current = root
            stack.append(current)
            stack.append([current.value])
            stack.append(current.value)
            while stack != []:
                pathsum = stack.pop()
                path = stack.pop()
                current = stack.pop()
                if current.left == None and current.right == None and pathsum == sum:
                    paths.append(path)
                if current.right:
                    rightpath = path + [current.right.value]    
                    stack.append(current.right)
                    stack.append(rightpath)
                    stack.append(pathsum + current.right.value)
                if current.left:
                    leftpath = path + [current.left.value]
                    stack.append(current.left)
                    stack.append(leftpath)
                    stack.append(pathsum + current.left.value)
        return paths
    