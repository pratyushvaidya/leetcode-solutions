# 152. MAXIMUM PRODUCT SUBARRAY

class Solution:
    """
    Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

    The test cases are generated so that the answer will fit in a 32-bit integer.

    A subarray is a contiguous subsequence of the array.

    Example 1:
    Input: nums = [2,3,-2,4]
    Output: 6
    Explanation: [2,3] has the largest product 6.
    
    Example 2:
    Input: nums = [-2,0,-1]
    Output: 0
    Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

    """
    def maxProduct(self, nums: List[int]) -> int:
        if min(nums)>0: return reduce(lambda x, y: x*y, nums)
        n = len(nums)
        dp = [[nums[0],nums[0]]] * n

        for i in range(1, n):
            if nums[i] == 0:
                dp[i] = [0,0]
            elif nums[i] > 0:
                dp[i] = [max(max(dp[i-1]) * nums[i], nums[i]), 
                         min(min(dp[i-1]) * nums[i], nums[i])]
            else:
                dp[i] = [max(min(dp[i-1]) * nums[i], nums[i]), 
                         min(max(dp[i-1]) * nums[i], nums[i])]
        return max(y[0] for y in dp)
                
