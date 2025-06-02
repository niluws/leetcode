from collections import Counter

class Solution:
    def intersect(self, nums1, nums2):
        counts = Counter(nums1)
        result = []

        for num in nums2:
            if counts[num] > 0:
                result.append(num)
                counts[num] -= 1
        return result



Solution().intersect([4,9,5,1,2,2,1], [2,1,1,9,4,9,8,4])
