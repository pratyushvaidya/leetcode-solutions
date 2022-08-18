# 101. SYMMETRIC TREE

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

    Example 1:
    Input: root = [1,2,2,3,4,4,3]
    Output: true
    
    Example 2:
    Input: root = [1,2,2,null,3,null,3]
    Output: false
    """
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left == None and root.right == None:
            return True
        if root.left == None or root.right==None:
            return False
        queue = [root.left,root.right]
        while len(queue):
            currLeft, currRight = queue.pop(0), queue.pop(0)
            if currLeft == None and currRight == None:
                continue
            elif currLeft == None or currRight == None:
                return False
            elif currLeft.val == currRight.val:
                queue.extend([currLeft.left, currRight.right, currLeft.right, currRight.left])
            else:
                 return False
        return True
