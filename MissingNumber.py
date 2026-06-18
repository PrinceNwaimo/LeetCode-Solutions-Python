class MissingNumber(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return None
        else:
            xor_prod = 0
            xor_prod_index = 0
            for i in range(len(nums)):
                xor_prod ^= nums[i]
            for i in range(len(nums)+1):
                xor_prod_index ^= i
            return xor_prod ^ xor_prod_index
