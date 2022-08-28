#226. INVERT BINARY TREE

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Given the root of a binary tree, invert the tree, and return its root.

    Example 1:
    Input: root = [4,2,7,1,3,6,9]
    Output: [4,7,2,9,6,3,1]

    Example 2:
    Input: root = [2,1,3]
    Output: [2,3,1]

    Example 3:
    Input: root = []
    Output: []
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        self.invertTree(root.left)
        self.invertTree(root.right)

        tempNode = root.left
        root.left = root.right
        root.right = tempNode

        return root
