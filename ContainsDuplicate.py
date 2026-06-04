class ContainsDuplicate(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        elif len(nums) == 1:
            return False
        else:
            dup_dict = {}
            for entries in nums:
                if entries in dup_dict:
                    return True
                else:
                    dup_dict[entries] = 1
            return False
