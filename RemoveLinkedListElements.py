class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class RemoveLinkedListElements(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return head
        elif head != None and head.next == None:
            if head.val == val:
                return None
            else:
                return head
        else:
            dummy = ListNode(0)
            dummy.next = head
            prev = dummy
            
            while head != None:
                if head.val == val:
                    prev.next = head.next
                    head = prev
                prev = head
                head = head.next
            return dummy.next
            