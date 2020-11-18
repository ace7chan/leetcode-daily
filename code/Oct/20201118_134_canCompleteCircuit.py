from typing import List
from itertools import accumulate


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        candidates = [i for i, (g, c) in enumerate(zip(gas, cost)) if g >= c]
        for candidate in candidates:
            g_tmp = accumulate(gas[candidate:] + gas[:candidate])
            c_tmp = accumulate(cost[candidate:] + cost[:candidate])
            if sum([g < c for g, c in zip(g_tmp, c_tmp)]) == 0:
                return candidate
        return -1


if __name__ == '__main__':
    solution = Solution()
    gas = [2, 3, 4]
    cost = [3, 4, 3]
    print(solution.canCompleteCircuit(gas, cost))
