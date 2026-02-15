class Solution:
    def addBinary(self, a: str, b: str) -> str:

        # bin method returns 0bXXXX
        a = int(a, 2)
        b = int(b, 2)

        sum = a + b

        return bin(sum)[2:]
        