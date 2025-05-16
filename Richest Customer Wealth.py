class Solution(object):
    def maximumWealth(self, accounts):
        wealth = []
        for account in accounts:
            wealth.append(sum(account))
        return max(wealth)

        # return max(sum(account) for account in accounts) #حافطه کم تر استفاده میشود


Solution().maximumWealth([[2, 8, 7], [7, 1, 3], [1, 9, 5]])
