from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left_idx, right_idx = -1, -1
        for i, num in enumerate(nums):
            if num == target:
                if left_idx == -1:
                    left_idx = i
                    right_idx = i
                else:
                    right_idx = i
        return [left_idx, right_idx]


if __name__ == '__main__':
    solution = Solution()
    nums = [5, 7, 7, 8, 8, 10]
    target = 8
    print(solution.searchRange(nums, target))
