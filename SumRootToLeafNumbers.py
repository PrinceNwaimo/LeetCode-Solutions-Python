from logging import root


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class SumRootToLeafNumbers(object):
    # @param {TreeNode} root
    # @return {integer}
    def sumNumbers(self, root):
        """:type root: TreeNode
        :rtype: int """
        if root == None:
            return 0
        else:
            stack = []
            paths = []
            stack.append(root)
            stack.append(str(root.val))
            while stack != []:
                path = stack.pop()
                current = stack.pop()
                if current.left == None and current.right == None:
                    paths.append(int(path))
                if current.right:
                    rightstr = path + str(current.right.val)
                    stack.append(current.right)
                    stack.append(rightstr)
                if current.left:
                    leftstr = path + str(current.left.val)
                    stack.append(current.left)
                    stack.append(leftstr)
            return sum(paths)
                