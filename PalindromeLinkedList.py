class PalindromeLinkedList(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return True
        elif head != None and head.next == None:
            return True
        else:
            fast = head
            slow = head
            stack = []
            while fast != None and fast.next != None:
                stack.append(slow.val)
                fast = fast.next.next
                slow = slow.next
                
                if fast == None:
                    slow = slow.next
            while slow != None:
                if slow.val != stack.pop():
                    return False
                else:
                    slow = slow.next
            return True
