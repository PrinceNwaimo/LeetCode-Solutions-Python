class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        else:
            fast = head
            slow = head
            
            has_cycle = False
            while fast != None and fast.next != None:
                fast = fast.next.next
                slow = slow.next
                
                if fast == slow:
                    has_cycle = True
                    break
            if has_cycle == False:
                return None
            slow = head
            while fast != slow:
                     fast = fast.next
                     slow = slow.next
                     
            return slow