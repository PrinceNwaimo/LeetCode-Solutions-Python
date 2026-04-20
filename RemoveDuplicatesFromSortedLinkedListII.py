from RemoveLinkedListElements import ListNode


class RemoveDuplicatesFromSortedLinkedListII(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        else:
            dup_dict = {}
            current = head
            while current != None:
                if current.val in dup_dict:
                    dup_dict[current.val] += 1
                else:
                    dup_dict[current.val] = 1
                current = current.next
                
                list_values = []
                current = head
            while current != None:
                if dup_dict[current.val] > 1:
                    pass
                else:
                    list_values.append(current.val)
                current = current.next
                if list_values == []:
                    return None
                else:
                    nodel = ListNode(list_values[0])
                    head = nodel
                    for entries in list_values[1:]:
                        new_nodel = ListNode(entries)
                        nodel.next = new_nodel
                        nodel = new_nodel
                    return head
                