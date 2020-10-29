# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.res = 0
        self.helper(root, [])
        return self.res

    def helper(self, node, char_list):
        if node:
            char_list.append(str(node.val))
            if node.left is None and node.right is None:
                self.res += int(''.join(char_list))
            if node.left:
                self.helper(node.left, char_list)
            if node.right:
                self.helper(node.right, char_list)
            char_list.pop()


if __name__ == '__main__':
    solution = Solution()
    a1, a2, a3 = TreeNode(1), TreeNode(2), TreeNode(3)
    a1.left = a2
    a1.right = a3
    print(solution.sumNumbers(a1))