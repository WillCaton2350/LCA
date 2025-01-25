class TreeNode(object):
    def __init__(self, _):
        self.val = _
        self.left = None
        self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left,p,q)
            # We are thinking about this as if we are reading the tree from left to right. 
        # Left node -> Root -> Right node / Left Subtree to Right Subtree
        # p -> root 
        # root -> q
        # Or 
        # q -> root 
        # root -> p
        elif root.val < p.val and root.val < q.val:
            return self.lowestCommonAncestor(root.right,p,q)
        else:
            return root
        # This is the recursive solution because the function calls itself with sub / nested conditions until a base case is met. 
        # Base Case == return root / sub problems == if and elif conditions
