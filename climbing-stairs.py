# 70. CLIMBING STAIRS

class Solution:
    """
    You are climbing a staircase. It takes n steps to reach the top.

    Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

    Example 1:
    Input: n = 2
    Output: 2
    Explanation: There are two ways to climb to the top.
    1. 1 step + 1 step
    2. 2 steps
    
    Example 2:
    Input: n = 3
    Output: 3
    Explanation: There are three ways to climb to the top.
    1. 1 step + 1 step + 1 step
    2. 1 step + 2 steps
    3. 2 steps + 1 step
    """
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        a0,a1,a2 = 1,1,0
        for i in range(1,n):
            a2 = a0 + a1
            a0 = a1
            a1 = a2
        return a2
