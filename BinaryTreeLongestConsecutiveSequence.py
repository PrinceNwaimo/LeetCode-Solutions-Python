class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

from queue import Queue
import sys
class BinaryTreeLongestConsecutiveSequence(object):
    # @param {TreeNode} root
    # @return {integer}
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        else:
            max_size = 1
            size_queue = Queue()
            node_queue = Queue()
            node_queue.put(root)
            size_queue.put(1)
            while not node_queue.empty():
                node = node_queue.get()
                size = size_queue.get()
                if node.left != None:
                    node_queue.put(node.left)
                    if node.value + 1 == node.left.value:
                        size_queue.put(size + 1)
                    else:
                        size_queue.put(1)
                if node.right != None:
                    node_queue.put(node.right)
                    if node.value + 1 == node.right.value:
                        size_queue.put(size + 1)
                    else:
                        size_queue.put(1)
                max_size = max(max_size, size)
            return max_size
        
        