from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        nums = [n for i, n in enumerate(nums) if i == 0 or nums[i] != nums[i - 1]]
        if len(nums) <= 2:
            return len(nums)
        is_up = nums[1] > nums[0]
        res = 2
        for i, num in enumerate(nums[2:]):
            if is_up and num < nums[i + 1]:
                is_up = False
                res += 1
            elif not is_up and num > nums[i + 1]:
                is_up = True
                res += 1
        return res


if __name__ == '__main__':
    solution = Solution()
    nums = [0, 0]
    print(solution.wiggleMaxLength(nums))
