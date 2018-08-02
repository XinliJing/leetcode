# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
    """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        return self.recursiveTree(root.left, root.right)
    
    def recursiveTree(self, leftRoot, rightRoot):
        if leftRoot is None and rightRoot is None:
            return True
        if leftRoot is None or rightRoot is None:
            return False
        if leftRoot.val == rightRoot.val:
            return self.recursiveTree(leftRoot.left, rightRoot.right) and self.recursiveTree(leftRoot.right, rightRoot.left)
        else:
            return False
