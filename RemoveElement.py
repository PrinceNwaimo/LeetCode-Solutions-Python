class RemoveElement(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if val == []:
            return 0
        else:
            count = 0
            zeroes = 0
            while count < len(nums):
                if nums[count] == val:
                    zeroes += 1
                else:
                    nums[count - zeroes] = nums[count]
                count += 1
            return len(nums) - zeroes
             