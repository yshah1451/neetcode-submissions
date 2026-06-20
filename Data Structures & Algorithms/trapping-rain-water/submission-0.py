class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        n = len(height)
        # 1. Initialize the arrays before assigning elements
        l = [0] * n
        r = [0] * n
        res = 0

        l[0] = height[0]
        r[n-1] = height[n-1]
        res = 0
        
        for i in range(1, n):
            l[i] = max(l[i-1],height[i])
            r[n-1-i] = max(r[n-1-i+1],height[n-1-i])

        for i in range(n):
            res = res + (min(l[i],r[i])-height[i])

        return res 