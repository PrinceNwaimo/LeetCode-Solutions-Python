import sys
class VerifyPreorderSequenceInBST(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        """
        stack = []
        root = -sys.maxsize-1
       
        for entries in preorder:
            if entries < root:
                return False
            while stack and entries > stack[-1]:
                root = stack.pop()
            stack.append(entries)
        return True
     