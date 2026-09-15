class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        res = max(weights)
        if len(weights) > 50:
            res = 9000
        while True:
            ships = 1
            capacity = res
            for w in weights:
                if capacity - w < 0:
                    ships += 1
                    capacity = res
                capacity -= w
            if ships <= days:
                return res
            res += 1