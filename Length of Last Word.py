class Solution:
    def lengthOfLastWord(self, s: str):
        index = len(list(s))

        count = 0
        while index > 0:
            if list(s)[index - 1] == " ":

                index -= 1
                if count > 0:
                    return count


            else:
                index -= 1
                count += 1

                if index<1 and count > 0:
                    return count






print(Solution().lengthOfLastWord("a"))
