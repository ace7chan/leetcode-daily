from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cur_idx = 0
        for num in nums:
            if num == 0:
                continue
            nums[cur_idx] = num
            cur_idx += 1
        while cur_idx < len(nums):
            nums[cur_idx] = 0
            cur_idx += 1
        # return nums


if __name__ == '__main__':
    solution = Solution()
    nums = [0, 1, 0, 3, 12]
    print(solution.moveZeroes(nums))
