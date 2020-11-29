from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        res = []
        self.helper(root, res)
        return res

    def helper(self, node, res):
        if node:
            res.append(node.val)
            if node.left:
                self.helper(node.left, res)
            if node.right:
                self.helper(node.right, res)


if __name__ == '__main__':
    n1, n2, n3 = TreeNode(1), TreeNode(2), TreeNode(3)
    n1.right = n2
    n2.left = n3
    solution = Solution()
    print(solution.preorderTraversal(n1))