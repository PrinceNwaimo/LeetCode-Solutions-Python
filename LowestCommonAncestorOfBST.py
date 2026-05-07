class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
class LowestCommonAncestorOfBST:
    def __init__(self):
        self.inorder_list = []
        self.postorder_list = []
        
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        else:
            self.inorder_traversal(root)
            self.postorder_traversal(root)
        #get the psoitions of node1 and node2 in the inorder traversal of the tree
        
        index_node1 = self.inorder_list.index(p.value)
        index_node2 = self.inorder_list.index(q.value)
        
        if index_node1 < index_node2:
            between_elements = self.inorder_list[index_node1:index_node2 + 1]
        else:
            between_elements = self.inorder_list[index_node2:index_node1 + 1]
        
        Lca_element = self.find_element_max_index(between_elements)
        return Lca_element
    
    def find_element_max_index(self, between_elements):   
         max_index = -1
         element = None
         for entries in between_elements:
           element_index = self.postorder_list.index(entries)
           if element_index > max_index:
               max_index = element_index
               element = entries
               return element
    def inorder_traversal(self, node):
        if node:
            self.inorder_traversal(node.left)
            self.inorder_list.append(node.value)
            self.inorder_traversal(node.right)   
    
    def postorder_traversal(self, node):
        if node:
            self.postorder_traversal(node.left)
            self.postorder_traversal(node.right)
            self.postorder_list.append(node.value)
            
                       
                
              