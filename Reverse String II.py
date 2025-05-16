class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        a = list(s)
        for i in range(0, len(a), 2 * k):
            a[i:i + k] = reversed(a[i:i + k])
        return "".join(a)


class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res=list(s)
        for i in range (0,len(s),k*2):
            res[i:i+k]=s[i:i+k][::-1]
        return ''.join(res)

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        chars = list(s)  # Convert string to list for in-place operations
        for i in range(0, len(s), 2 * k):
            # Reverse the first k characters in every 2k block
            chars[i:i+k] = reversed(chars[i:i+k])
        return ''.join(chars)


Solution().reverseStr("abcdefg", 2)
