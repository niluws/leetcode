class Solution(object):
    def twoSum(self, nums, target):
        lookup = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in lookup:
                return [lookup[complement], i]
            lookup[num] = i

            print(lookup)




Solution().twoSum([3, 9,2, 4, 0, 1], 6)

# [3,6,2,1,9] ,5
