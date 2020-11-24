# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def countNodes(self, root: TreeNode) -> int:
        return self.helper(root)

    def helper(self, node):
        if node is None:
            return 0
        elif node.left and node.right:
            return 1+self.helper(node.left) + self.helper(node.right)
        elif node.left:
            return 1+self.helper(node.left)
        else:
            return 1+self.helper(node.right)

if __name__ == '__main__':
    solution = Solution()
    a1 = TreeNode(1)
    a2, a3 = TreeNode(2), TreeNode(3)
    a1.left = a2
    a1.right = a3
    print(solution.countNodes(a1))