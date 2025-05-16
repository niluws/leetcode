class Solution:
    def sortArrayByParity(self,nums):
        evens = []
        odds = []

        for num in nums:
            if num % 2 == 0:
                evens+=[num]
            else:
                odds+=[num]

        return evens + odds


Solution().sortArrayByParity([3,2,1])
