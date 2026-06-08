class MoveZeroes(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        zeroes = 0
        number_of_zeroes = 0
        
        while zeroes < len(nums):
            if nums[zeroes] == 0:
                number_of_zeroes += 1
            else:
                nums[zeroes - number_of_zeroes] = nums[zeroes]
            zeroes += 1
        
        while zeroes < len(nums):
            nums[zeroes] = 0
            zeroes += 1
            
                