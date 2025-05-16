class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        word_vowels = []
        
        for char in s:

            if char in vowels:
                word_vowels += char
        index = 0
        word_vowels = word_vowels[::-1]

        s = list(s)
        for char in range(len(s)):

            if s[char] in vowels:
                s[char] = word_vowels[index]

                index += 1

        return ''.join(s)


print(Solution().reverseVowels('leetcode'))
