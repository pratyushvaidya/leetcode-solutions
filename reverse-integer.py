# 7. REVERSE INTEGER

class Solution:
    """
    Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

    Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

    Example 1:
    Input: x = 123
    Output: 321
    
    Example 2:
    Input: x = -123
    Output: -321
    
    Example 3:
    Input: x = 120
    Output: 21
    """
    def reverse(self, x: int) -> int:
        maxPos, maxNeg, isNeg = (2**31) - 1, (2**31), (x < 0)
        l = str(abs(x))[::-1]
        
        if len(l) <= 9:
            return int(str(abs(x))[::-1]) * -1 if isNeg else int(str(abs(x))[::-1])
        if isNeg and l <= str(maxNeg):
            res = 0
            for i in l:
                res = (res * 10) - int(i)
            return res
        if not isNeg and l <= str(maxPos):
            return int(str(abs(x))[::-1])
        return 0
