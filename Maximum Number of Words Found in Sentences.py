class Solution(object):
    def mostWordsFound(self, sentences):
        nums = []
        for i in sentences:
            nums.append(len(i.split()))

        return max(nums)


Solution().mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"])
