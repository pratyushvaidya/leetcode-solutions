#437. PATH SUM III

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Given the root of a binary tree and an integer targetSum, return the number of paths where the sum of the values along the path equals targetSum.

    The path does not need to start or end at the root or a leaf, but it must go downwards (i.e., traveling only from parent nodes to child nodes).

    Example 1:
    Input: root = [10,5,-3,3,2,null,11,3,-2,null,1], targetSum = 8
    Output: 3
    Explanation: The paths that sum to 8 are shown.
    
    Example 2:
    Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
    Output: 3

    """
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.count, currSum, sumMap = 0, 0, defaultdict(int)

        def traverse(current: Optional[TreeNode], currSum: int):
            if not current:
                return

            currSum += current.val
            if currSum == targetSum:
                self.count += 1
            if sumMap.get(currSum - targetSum):
                self.count += sumMap[currSum - targetSum]

            sumMap[currSum] += 1

            traverse(current.left, currSum)
            traverse(current.right, currSum)

            sumMap[currSum] -= 1

        traverse(root, 0)
        return self.count
