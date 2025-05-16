class Solution:
    def plusOne(self, digits):
        n = len(digits) - 1
        while n >= 0:
            if digits[n] < 9:
                digits[n] += 1
                return digits
            else:
                digits[n] = 0
                n -= 1
        return [1] + digits


print(Solution().plusOne([1, 2, 3]))
print(Solution().plusOne([4, 3, 2, 1]))
print(Solution().plusOne([9]))
print(Solution().plusOne([9, 9, 9]))
