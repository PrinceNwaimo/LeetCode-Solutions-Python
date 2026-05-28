from queue import Queue


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTreeZigzagLevelOrderTraversal(object):
    # @param {TreeNode} root
    # @return {integer[][]}
    def zigzagLevelOrder(self, root):
        if root == None:
            return []
        else:
             queer = Queue.Queue()
             queer.put(root)
             queer.put("#")
             levelOrderTraversal = []
             level = []
             levelNo = 0
        while queer.empty() == False:
                node = queer.get()
                if node == "#":
                    if queer.empty() == False:
                        queer.put("#")
                    if levelNo == 0 or levelNo % 2 == 0:    
                        levelOrderTraversal.append(level)
                    else:
                        levelOrderTraversal.append(level[::-1])
                    level = []
                    levelNo += 1
                else:
                    level.append(node.val)
                    if node.left:
                        queer.put(node.left)
                    if node.right:
                        queer.put(node.right)    
        return levelOrderTraversal
    