from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        last_up = len(nums) - 2
        while last_up >= 0 and nums[last_up] >= nums[last_up + 1]:
            last_up -= 1
        if last_up == -1:
            nums[:] = nums[::-1]
        else:
            first_large = len(nums) - 1
            last_up_val = nums[last_up]
            while first_large >= 0 and nums[first_large] <= last_up_val:
                first_large -= 1
            if first_large == -1:
                nums[:] = nums[::-1]
            else:
                nums[last_up] = nums[first_large]
                nums[first_large] = last_up_val
                nums[last_up + 1:] = nums[last_up + 1:][::-1]
        print(nums)


if __name__ == '__main__':
    solution = Solution()
    nums = [5, 1, 1]
    solution.nextPermutation(nums)
