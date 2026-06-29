class Subsets2(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        n = 1 << len(nums)
        result = []
        for i in range(0, n):
            subset = self.convert(i, nums)
            result.append(subset)
        return result
    def convert(self, i, nums):
        k = i
        index = 0
        subset = []
        while k > 0:
            if k & 1 == 1:
                subset.append(nums[index])
            index += 1
            k >>= 1
        return subset
    
    