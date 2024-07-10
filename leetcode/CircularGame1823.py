class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        freinds = []
        for i in range(n):
            freinds.append(n + 1)
        index = k - 1
        while len(freinds) != 1:
            freinds.pop(index)
            index += k - 1
            index = n % index
        return freinds[0]

