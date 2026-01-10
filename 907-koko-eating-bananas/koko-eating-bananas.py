class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        n = len(piles)
        small = 1
        large = max(piles)
        
        while small <= large:
            temp = 0
            avg = (small + large) // 2
            for i in range(n):
                if avg >= piles[i]:
                    temp += 1
                if avg < piles[i]:
                    temp += ceil(piles[i] / avg)   
            print(temp, avg) 
            if temp <= h:
                large = avg - 1
            else:
                small = avg + 1     
                   
        return small