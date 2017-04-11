'''
https://leetcode.com/problems/invert-binary-tree/#/description

Problem:

    
Example:
     4

   /   \

  2     7

 / \   / \

1   3 6   9

:author: babykick
:date: 2017-04-11
'''


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if root == None:
            return None
        if root.left == None and root.right == None:      # Single node or leaf
            return root
        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
        
        
        

if __name__ == '__main__':
    single = TreeNode(4)
    r = TreeNode(4)
    r.left = TreeNode(2)
    r.right = TreeNode(7)
    r.left.left = TreeNode(1)
    r.left.right = TreeNode(3)
    r.right.left = TreeNode(6)
    r.right.right = TreeNode(9)


    test_cases = [
        # tuple of (input, output)
        (single, single),
        (r, r),
    ]
    
    for sample in test_cases:
        inp, outp = sample
        r = inp
        Solution().invertTree(r)
        if r.left and r.right:
            print(r.val)
            print(r.left.val, r.right.val)
            print(r.left.left.val, r.left.right.val)
            print(r.right.left.val, r.right.right.val)
         
        #assert r_.left == r.right
        #assert(Solution().unknown(inp) == outp)
    
