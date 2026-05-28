from logging import root
from unittest import result


class TreeNode(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class HouseRobber3(object):
    # @param {TreeNode} root
    # @return {integer}
    def rob(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            result = self.rob_max(root)
            return max(result[0], result[1])
    
    def rob_max(self, root):
        if root == None:
            return [0, 0]
        else:
            left_res = self.rob_max(root.left)
            right_res = self.rob_max(root.right)
            result = [0]*2
            result[0] = root.val + left_res[1] + right_res[1]
            result[1] = max(left_res[0], left_res[1]) + max(right_res[0], right_res[1])
            return result