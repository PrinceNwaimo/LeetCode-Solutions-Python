class SummaryRanges(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if nums == []:
            return nums
        elif len(nums) == 1:
            return [str(nums[0])]
        else:
            start = nums[0]
            end = nums[0]
            res = []
            for i in range(1, len(nums)):
                if nums[i] - nums[i-1] == 1:
                    end = nums[i]
                else:
                    res.append(self.to_str(start, end))
                    start = end = nums[i]
            res.append(self.to_str(start, end))
            return res  
        
    def to_str(self, start, end):
        if start == end:
            return str(start)
        else:
            return str(start) + "->" + str(end)