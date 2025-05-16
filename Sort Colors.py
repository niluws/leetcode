# 0 ,1 ,2 = red, white,blue
# sort red ,white, blue

class Solution(object):
    def sortColors(self, nums):
        i = len(nums) - 1

        j = 0

        while j <= i:
            if nums[j] > nums[i]:
                max_index = j
                nums[i], nums[j] = nums[max_index], nums[i]

                i -= 1
            else:
                j += 1
        return nums


print(Solution().sortColors([1,0,2]))
