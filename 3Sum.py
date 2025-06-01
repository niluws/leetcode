class Solution:
    def threeSum(self, nums):
        j=0
        k=0
        for i in range(len(nums)):
            if j==i:
                j+=1
            elif k==i:
                k+=1
            elif k==j:
                j+=1

            print(i,j)

print(Solution().threeSum([-1,0,1,2,-1,-4]))