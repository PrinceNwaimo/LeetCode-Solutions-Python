class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class RecoverBST(object):
    def __init__(self):
        self.__prev = None
        self.__node1 = None
        self.__node2 = None
    def recoverTree(self, root):
        """ :type root: TreeNode :rtype: void Do not return anything, modify root in-place instead. """
        self.recoverTreeHelper(root)
        temp = self.__node1.value
        self.__node1.value = self.__node2.value
        self.__node2.value = temp
    def recoverTreeHelper(self, root):
        if root == None:
            return
        self.recoverTreeHelper(root.left)
        if self.__prev != None and self.__prev.value > root.value:
            if self.__node1 == None:
                self.__node1 = self.__prev
            self.__node2 = root
        self.__prev = root
        self.recoverTreeHelper(root.right)
                