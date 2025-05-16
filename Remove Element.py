# class Solution:
#     def removeElement(self, nums, val: int) -> int:
#         k = 0 #slower
#         for i in range(len(nums)):#faster
#             if nums[i] != val:
#                 nums[k] = nums[i]
#                 k += 1
#
#         return k

class Solution:
    def removeElement(self, nums, val: int) -> int:
        L = 0
        k = 0
        for num in nums:
            if num != val:
                nums[L] = num
                k += 1
                L += 1
        return k

print(Solution().removeElement([2], 3))

