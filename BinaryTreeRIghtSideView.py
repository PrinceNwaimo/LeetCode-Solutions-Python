class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
from multiprocessing import Queue
      
class BinaryTreeRightSideView(object):
     # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
         if root == None:
            return []
         else:
            queer = Queue.Queue()
            queer.put(root)
            queer.put("#")
            rightSideView = []
            level = []
            while queer.empty() == False:
                node = queer.get()
                if node == "#":
                    if queer.empty() == False:
                        queer.put("#")
                    rightSideView.append(level[-1])
                    level = []
                else:
                    level.append(node.val)
                    if node.left != None:
                        queer.put(node.left)
                    if node.right != None:
                        queer.put(node.right)
            return rightSideView