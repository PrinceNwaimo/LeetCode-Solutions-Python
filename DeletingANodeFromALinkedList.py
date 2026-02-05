#Defintion fro sigly-linked list
# // class ListNode(object):
# //     def __init__(self, x):         
# //         self.val = x
# //         self.next = None
class Solution(object):
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        if node == None:
            pass
        else:
            next_node = node.next
            node.val = next_node.val
            node.next = next_node.next
            next_node = None
        return
# Definition for singly-linked list.
# // class ListNode(object):
# //     def __init__(self, x):
# //         self.val = x
# //         self.next = None
class Solution(object):
    def reversedList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        elif head != None and head.next == None:
            return head
        else:
            temp = None
            next_node = None
            while head != None:
                next_node = head.next
                head.next = temp
                temp = head
                head = next_node
            return temp     
# Definition for singly-linked list.
# // class ListNode(object):    
# //     def __init__(self, x):
# //         self.val = x
# //         self.next = None
class Solution(object):
    def reversedList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return None
        elif head != None and head.next == None:
            return head
        else:
            temp = None
            next_node = None
            while head != None:
                next_node = head.next
                head.next = temp
                temp = head
                head = next_node
            return temp