# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # strategy: we know the first element of preorder is the root
        # we then find the index of this element in inorder which will tell us which elements split left and right of the root
        # then recurse into left and right subtrees and do the same
        
        i_indices = {}
        for i in range(len(inorder)):
            i_indices[inorder[i]] = i
        
        
        def build(preorder_idx, left, right):
            if left > right:
                return None

            root_val = preorder[preorder_idx]
            root = TreeNode(root_val)

            root_index = i_indices[root_val]

            left_size = root_index - left


            root.left = build(
                preorder_idx + 1,
                left,
                root_index - 1
            )


            root.right = build(
                preorder_idx + 1 + left_size,
                root_index + 1,
                right
            )

            return root

        return build(0, 0, len(inorder) - 1)

        