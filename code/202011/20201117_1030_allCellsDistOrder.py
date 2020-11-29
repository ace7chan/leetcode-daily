from typing import List


class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        res = []
        for r in range(R):
            for c in range(C):
                res.append(((r, c), abs(r - r0) + abs(c - c0)))
        res = sorted(res, key=lambda k: k[1])
        return [r[0] for r in res]


if __name__ == '__main__':
    solution = Solution()
    print(solution.allCellsDistOrder(2, 2, 0, 1))
