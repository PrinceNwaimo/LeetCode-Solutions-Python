class ContainsNearbyDuplicate(object):

    def containsNearbyDuplicate(self, nums, k):         
        """         
        :type nums: List[int]
        :type k: int         
        :rtype: bool         
        """
        
        if not nums:             
            return False
        elif len(nums) == 1:             
            return False
        index_dict = {}
        for i in range(len(nums)):
            if nums[i] in index_dict:
                prev_index = index_dict[nums[i]]
                if i - prev_index <= k:
                    return True
            index_dict[nums[i]] = i
        return False
