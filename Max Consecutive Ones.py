from typing import List


class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        consecutive = 0
        max_consecutive = 0
        for i in range(len(nums)):
            if nums[i] == 1:

                consecutive += 1

                max_consecutive=max(max_consecutive,consecutive)
            else:
                consecutive = 0

        return max_consecutive


print(Solution().findMaxConsecutiveOnes([1, 0, 1, 1, 0, 1, 0, 1, 1]))

