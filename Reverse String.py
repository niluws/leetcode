class Solution:
    def reverseString(self, s) -> None:
        j = 0

        for i in s[::-1]:
            s[j] = i
            j += 1
        return s


print(Solution().reverseString(["h", "e", "l", "l", "o"]))
