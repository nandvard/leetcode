# https://leetcode.com/problems/binary-tree-maximum-path-sum/

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxPathSum(self, root):
        """
        If all values are positive, to find max path sum,
        get 1-child max path of left subtree, and 1-child max path of right subtree
        note global path sum as sum of root + left1 + right1
        get max of left1,right1 and add it to root to return max 1-child path including root
        
        If any of left/right values are negative, just truncate them to 0
        """
        
        def path1sum_(root):
            if not root:
                return 0
            
            left1 = path1sum_(root.left)
            right1 = path1sum_(root.right)

            # Add these 2 lines if values are -ve
            left1 = max(left1,0)
            right1 = max(right1,0)
            
            root1 = root.val + max(left1,right1)
            
            self.max_path = max(self.max_path, root.val + left1 + right1)       # global max
            
            return root1
        
        
        self.max_path = None
        
        path1sum_(root)
        
        return self.max_path
