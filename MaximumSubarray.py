import sys 
class MaximumSubarray(object):
    def maxSubArray(self, nums):         
        """
        :type nums: List[int]         
        :rtype: int        
        """
        if nums == []:             
            return 0
        elif len(nums) == 1:             
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1], nums[0]+nums[1])         
        else:             
            all_neg = True
            for entries in nums:
                if entries >= 0:
                    all_neg = False
            if all_neg == False:
                curr_sum = 0                 
                max_sum = sys.maxsize - 1
                for i in range(len(nums)):
                    curr_sum += nums[i]
                    if curr_sum < 0:
                        curr_sum = 0
                    if curr_sum > max_sum:
                        max_sum = curr_sum
                return max_sum            
            else:
                return max(nums)
