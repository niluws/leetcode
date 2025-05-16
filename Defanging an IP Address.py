class Solution:
    def defangIPaddr(self, address: str) -> str:
        print(address.replace('.', '[.]'))
        return address.replace('.', '[.]')

Solution().defangIPaddr('1.1.1.1')
