class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        total = 0

        for char in word:
            if "A" <= char <= 'Z':
                total += 1

        if total == 1 and "A" <= list(word)[0] <= 'Z' or total == len(word) or total==0 :
            return True
        return False


print(Solution().detectCapitalUse("ggg"))
