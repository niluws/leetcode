from collections import Counter


class Solution(object):
    def singleNumber(self, nums):
        count = Counter(nums)
        for num in nums:
            if count[num] == 1:
                return num


Solution().singleNumber([2, 2, 1, 1])
