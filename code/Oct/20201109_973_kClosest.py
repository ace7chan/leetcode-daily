from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        points = sorted(points, key=lambda key: key[0] ** 2 + key[1] ** 2)
        return points[:K]


if __name__ == '__main__':
    solution = Solution()
    points = [[3, 3], [5, -1], [-2, 4]]
    K = 2
    print(solution.kClosest(points, K))
