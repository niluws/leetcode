class Solution(object):
    def rotate(self, nums, k):
        k %= len(nums)
        nums[:] = nums[-k:] + nums[:-k]
        return nums


print(Solution().rotate([1,2], 3))
