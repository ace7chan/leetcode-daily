# from typing import List
#
#
# class Solution:
#     def countRangeSumv2(self, nums: List[int], lower: int, upper: int) -> int:
#         nums_len = len(nums)
#         res = 0
#         for i in range(nums_len):
#             cur_val = nums[i]
#             if lower <= cur_val <= upper:
#                 res += 1
#             for j in range(i + 1, nums_len):
#                 cur_val += nums[j]
#                 if lower <= cur_val <= upper:
#                     res += 1
#         return res
#
#
# if __name__ == '__main__':
#     solution = Solution()
#     nums, lower, upper = [-2, 5, -1], -2, 2
#     print(solution.countRangeSum(nums, lower, upper))
