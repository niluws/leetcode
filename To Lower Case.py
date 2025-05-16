class Solution:
    def toLowerCase(self, s: str) -> str:
        for char in s:

            if 'A' <= char <= 'Z':
                s = s.replace(char, chr(ord(char) + 32))
        return s

print(Solution().toLowerCase("Hello"))
