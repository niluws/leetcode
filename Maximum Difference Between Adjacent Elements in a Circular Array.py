from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        result = 0

        for i in range(len(nums)):
            if i == len(nums) - 1:

                sub = max(nums[i], nums[0]) - min(nums[i], nums[0])

            else:
                sub = max(nums[i], nums[i + 1]) - min(nums[i], nums[i + 1])

            if result < sub:
                result = sub

        return result


Solution().maxAdjacentDistance([4, 3,100, 2])
