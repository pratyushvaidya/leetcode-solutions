# 283. MOVE ZEROES

class Solution:
    """
    Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

    Note that you must do this in-place without making a copy of the array.

    Example 1:
    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0]
    
    Example 2:
    Input: nums = [0]
    Output: [0]
    """
    def moveZeroes(self, nums: List[int]) -> None:
        i,j = 0,0
        while j != len(nums):
            if nums[j] != 0:
                nums[i] = nums[j]
                i,j = i+1,j+1
            else:
                j += 1
        while i!= len(nums):
            nums[i] = 0
            i += 1
