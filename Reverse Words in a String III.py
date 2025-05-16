class Solution:
    def reverseWords(self, s: str) -> str:
        s = list(s)
        n = len(s)
        start = 0
        for i in range(n + 1):
            if i == n or s[i] == ' ':
                end=i - 1
                while start < end:
                    s[start], s[end] = s[end], s[start]
                    start += 1
                    end -= 1
                start = i + 1
        return ''.join(s)


Solution().reverseWords("Mr Ding")
