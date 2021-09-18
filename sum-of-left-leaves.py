# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 0
        if root.left:
            if root.left.left == None and root.left.right == None:
                return root.left.val + self.sumOfLeftLeaves(root.right)
            return self.sumOfLeftLeaves(root.right) + self.sumOfLeftLeaves(root.left)
        if root.right:
            return self.sumOfLeftLeaves(root.right)

        return self.sumOfLeftLeaves(root.right) + self.sumOfLeftLeaves(root.left)