import heapq
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None
class MergeKSortedLinkedLists(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if lists == [] or lists == None:
            return None
        else:
            pq = []
            for i in range(len(lists)):
                if lists[i] != None:
                    item = (lists[i].val, i, lists[i])
                    heapq.heappush(pq, item)
        dummy = ListNode(0)
        tail = dummy    
        while pq:
            node = heapq.heappop(pq)
            tail.next = node[2]
            tail = tail.next
            if node[2].next != None:
                item = (node[2].next.val, node[1], node[2].next)
                heapq.heappush(pq, item)
        return dummy.next
                