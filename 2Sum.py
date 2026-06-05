class TwoSum(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_dict = {}
        for i in range(len(nums)):
            x = nums[i]
            if target - x in num_dict:
                return (num_dict[target - x], i)
            num_dict[x] = i
if __name__ == "__main__":
    soln = TwoSum()
    print(soln.twoSum([2, 7, 11, 15], 9))   
    