class MergeSortedArrays(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        count = m + n - 1
        count1 = m - 1
        count2 = n - 1
        
        while count >= 0:
            if count2 < 0:
                break
            elif count1 < 0:
                nums1[count] = nums2[count2]
                count2 -= 1
            elif nums1[count1] > nums2[count2]:
                nums1[count] = nums1[count1]
                count1 -= 1
            else:
                nums1[count] = nums2[count2]
                count2 -= 1
            count -= 1