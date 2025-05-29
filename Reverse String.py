class Solution:
    def reverseString(self, s) -> None:
        s[:]=s[::-1]
        return s


print(Solution().reverseString(["h", "e", "l", "l", "o"]))
