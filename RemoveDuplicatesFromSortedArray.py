class RemoveDuplicatesFromSortedArray(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int         
        """
        if len(nums) < 2:
            return len(nums)
        else:  
            zeros = 0
            index = 1
            while index < len(nums):
                if nums[index] == nums[index - 1]:
                    zeros += 1
                else:
                    nums[index - zeros] = nums[index]
                index += 1
                return zeros + 1
            