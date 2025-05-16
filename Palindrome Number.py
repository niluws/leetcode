class Solution:
    def isPalindrome(self, x: int) -> bool:

        r = 0
        temp = x
        while temp > 0:
            r = r * 10 + (temp % 10)
            temp = temp // 10
        return r == x



print(Solution().isPalindrome(121))
print(Solution().isPalindrome(-121))
print(Solution().isPalindrome(10))