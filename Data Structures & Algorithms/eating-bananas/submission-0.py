class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l <= r:
            mid = (l+r) // 2

            time_spent = 0
            for p in piles:
                time_pile = math.ceil(p / mid)
                time_spent += time_pile 
            
            if time_spent <= h:
                res = mid 
                r = mid - 1
            else:
                l = mid + 1
            
        return res
        