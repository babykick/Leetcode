'''
https://leetcode.com/problems/maximum-depth-of-binary-tree/#/description

Problem:
Given a binary tree, find its maximum depth.
    
Example:
The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

:author: babykick
:date: 2017-04-09
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: 
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))
      
         

if __name__ == '__main__':
    r1 = TreeNode(4)
    r2= TreeNode(4)
    r2.left = TreeNode(3)
  
    r3= TreeNode(4)
    r3.left = TreeNode(3)
    r3.right = TreeNode(1)

    r4= TreeNode(4)
    r4.left = TreeNode(3)
    r4.right = TreeNode(1)
    r4.right.left = TreeNode(2)
    test_cases = [
        # tuple of (input, output)
        (r1, 1),
        (r2, 2),
        (r3, 2),
        (r4, 3)
        
    ]
    
    for sample in test_cases:
        inp, outp = sample
      
        print(Solution().maxDepth(inp), outp)
    
