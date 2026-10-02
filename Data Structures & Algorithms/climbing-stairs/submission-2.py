class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0] * (n+1)
        if n > 0:
            ways[1] = 1
        if n > 1:
            ways[2] = 2
        for i in range(3, n+1):
            ways[i] = ways[i-1] + ways[i-2]
        return ways[n]
        