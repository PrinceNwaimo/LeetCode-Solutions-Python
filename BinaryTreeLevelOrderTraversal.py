class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
from queue import Queue
class BinaryTreeLevelOrderTraversal(object):
    def levelOrder(self, root):
        if root == None:
            return []
        else:
            q= Queue.Queue()
            q.put(root)
            levelOrderTraversal = []
            level = []
            while q.empty() == False:
                node = q.get()
                if node == "#":
                    if q.empty() == False:
                        q.put("#")
                    levelOrderTraversal.append(level)
                    level = []
                else:
                    level.append(node.value)
                    if node.left != None:
                        q.put(node.left)
                    if node.right != None:
                        q.put(node.right)
            return levelOrderTraversal
        