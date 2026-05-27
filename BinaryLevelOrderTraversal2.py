class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
        
from collections import Queue
class BinaryLevelOrderTraversal2(object):
    def levelOrderBottom(self, root):
        """ :type root: TreeNode :rtype: List[List[int]] """
        if root == None:
            return []
        else:
             queer = Queue.Queue()
             queer.put(root)
             queer.put("#")
             levelOrderTraversal = []
             level = []
             stack = []
             
             while queer.empty() == False:
                 current = queer.get()
                 if current == "#":
                     stack.append(level)
                     level = []
                     if queer.empty() == False:
                         queer.put("#")
                 else:
                     level.append(current.value)
                     if current.left:
                         queer.put(current.left)
                     if current.right:
                         queer.put(current.right)
                    
        while stack:    
            levelOrderTraversal.append(stack.pop())
        return levelOrderTraversal
                    