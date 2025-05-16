class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        result = ""

        while columnNumber > 0:
            columnNumber -= 1
            result = letters[columnNumber % 26] + result
            columnNumber //= 26
        return result

print(Solution().convertToTitle(286))
#
print(2)