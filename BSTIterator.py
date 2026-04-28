class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class BSTIterator:
 def __init__(self,root):
    self.stack = []
    node = root
    while node != None:
        self.stack.append(node)
        node = node.left
        
        
    def hasNext(self):
        return len(self.stack) != 0
    
    def next(self):
        nextNode = self.stack.pop()
        currentNode = nextNode.right
        while currentNode != None:
            self.stack.append(currentNode)
            currentNode = currentNode.left      
        return nextNode.val
    
# Your BSTIterator will be called like this:
# i = BSTIterator(root)
# while i.hasNext(): print(i.next())


        
              