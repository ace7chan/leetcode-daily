from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        res = sum([max(prices[i] - prices[i - 1], 0) for i in range(1, len(prices))])
        return res


if __name__ == '__main__':
    solution = Solution()
    prices = [7, 1, 5, 3, 6, 4]
    print(solution.maxProfit(prices))
