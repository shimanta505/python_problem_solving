class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        bottles = numBottles
        while(numBottles >= numExchange):
            prevNumBottles = numBottles
            numBottles = numBottles // numExchange
            bottles += numBottles
            numBottles += prevNumBottles % numExchange
        return bottles

