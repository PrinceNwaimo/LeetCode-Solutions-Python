class IntersectionOfTwoArraysII(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        sorted1 = sorted(nums1)
        sorted2 = sorted(nums2)
        
        count = 0
        count2 = 0
        result = []
        while count < len(sorted1) and count2 < len(sorted2):
            if sorted1[count] == sorted2[count2]:
                result.append(sorted1[count])
                count += 1
                count2 += 1
            elif sorted1[count] < sorted2[count2]:
                count += 1
            else:
                count2 += 1
        return result
    