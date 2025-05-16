class Solution:
    def removeDuplicates(self, nums) -> int:
        k = 0
        count = 0
        for i in range(1, len(nums)):

            count += 1

            if nums[k] != nums[i] and count >= 2:
                nums[k + 2] = nums[i]
                k += 1

                count = 1

        return k + 2




print(Solution().removeDuplicates([1, 1, 1,1, 2, 2,2,3 ,3,4]))
