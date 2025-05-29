class Solution(object):
    def reverse(self, x):
        absolute = abs(x)
        x = int(f'-{(str(absolute))[::-1]}') if x != absolute else int((str(x))[::-1])

        x = 0 if x < -2 ** 31 or x > 2 ** 31 - 1 else x

        return x


print(Solution().reverse(-1534236469))
