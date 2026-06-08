class MajorityElement(object):
    def majorityElement(self, nums):
        """         
        :type nums: List[int]
        :rtype: int         
        """
        candidate = self.get_candidate(nums)         
        candidate_count = 0
        if candidate != None:
            for entries in nums:
                if entries == candidate:
                    candidate_count += 1
            if candidate_count >= len(nums)//2:                 
                return candidate
            else:                 
                return None
        else:             
            return None
    def get_candidate(self, nums):
        count = 0
        candidate = None
        for entries in nums:
            if count == 0:
                candidate = entries
                count = 1
            else:
                if candidate == entries:
                    count += 1
                else:
                    count -= 1
        if count > 0:
            return candidate
        else:
            return None    