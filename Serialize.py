class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Serialize:
    def __init__(self):
        self.serialized_array = []
        self.index = 0
    def serialize(self, root):
        """Encodes a tree to a single string.
        :type root: TreeNode
        :rtype: str
        """
        self.serialized_help(root)
        return self.serialized_array
    def serialized_help(self, root):
        if root == None:
            self.serialized_array.append(None)
            return
        
        self.serialized_array.append(root.val)
        self.serialized_help(root.left)
        self.serialized_help(root.right)
            
    def deserialize(self, data):
        """Decodes your encoded data to tree.
        :type data: str
        :rtype: TreeNode
        """
        if self.index >= len(data) or data[self.index] == None:
            self.index += 1
            return None
        root = TreeNode(data[self.index])
        self.index += 1
        root.left = self.deserialize(data)
        root.right = self.deserialize(data)
        return root
    