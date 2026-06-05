class ThreeSum(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []

        sum_zero_list = []
        sorted_nums = sorted(nums)
        for i in range(0, len(sorted_nums) - 2):
            # skip duplicates for the first element
            if i > 0 and sorted_nums[i] == sorted_nums[i - 1]:
                continue

            start = i + 1
            end = len(sorted_nums) - 1
            while start < end:
                curr_sum = sorted_nums[i] + sorted_nums[start] + sorted_nums[end]
                if curr_sum == 0:
                    zero_triplet = (sorted_nums[i], sorted_nums[start], sorted_nums[end])
                    sum_zero_list.append(zero_triplet)
                    # move both pointers and skip duplicates
                    start += 1
                    end -= 1
                    while start < end and sorted_nums[start] == sorted_nums[start - 1]:
                        start += 1
                    while start < end and sorted_nums[end] == sorted_nums[end + 1]:
                        end -= 1
                elif curr_sum < 0:
                    start += 1
                else:
                    end -= 1

        return [list(entries) for entries in set(sum_zero_list)]


if __name__ == "__main__":
    soln = ThreeSum()
    print(soln.threeSum([-1, 0, 1, 2, -1, -4]))