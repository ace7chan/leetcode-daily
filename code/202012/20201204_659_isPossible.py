from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        num2cnt = dict()
        tails = dict()
        for num in nums:
            num2cnt[num] = num2cnt.get(num, 0) + 1
            tails[num] = 0
        for num in nums:
            if num2cnt[num] == 0:
                continue
            if (num - 1 in tails) and (tails[num - 1] > 0):
                num2cnt[num] -= 1
                tails[num - 1] -= 1
                tails[num] += 1
            elif (num + 1 in num2cnt) and (num + 2 in num2cnt) and (num2cnt[num + 1] > 0) and (num2cnt[num + 2] > 0):
                for i in range(3):
                    num2cnt[num + i] -= 1
                tails[num + 2] += 1
            else:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    nums = [1, 2, 3, 4]
    print(solution.isPossible(nums))
