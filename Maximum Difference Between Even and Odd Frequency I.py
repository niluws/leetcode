from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        count = Counter(s)
        odd = [count[i] for i in count if count[i] % 2 != 0]
        even = [count[i] for i in count if count[i] % 2 == 0]

        return max(odd) - min(even)


Solution().maxDifference("eedaaaqqqasssssbbbcf")
