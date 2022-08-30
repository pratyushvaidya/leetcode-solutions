# 75. SORT COLORS

class Solution:
    """
    Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white, and blue.

    We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

    You must solve this problem without using the library's sort function.

    Example 1:
    Input: nums = [2,0,2,1,1,0]
    Output: [0,0,1,1,2,2]
    
    Example 2:
    Input: nums = [2,0,1]
    Output: [0,1,2]
    """
    def sortColors(self, nums: List[int]) -> None:
        i,j,k = 0,len(nums)-1,0
        while k <= j:
            if nums[k] == 1: k+=1
            elif nums[k] == 2: 
                t = nums[k]
                nums[k] = nums[j]
                nums[j] = t
                j-=1
            else:
                t = nums[i]
                nums[i] = nums[k]
                nums[k] = t
                i+=1
                k+=1
