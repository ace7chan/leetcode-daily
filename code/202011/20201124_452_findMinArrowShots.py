from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if len(points) == 0:
            return 0
        points = sorted(points, key=lambda v: (v[0], v[1]))
        new_list = [points[0]]
        for point in points[1:]:
            if point[0] > new_list[-1][1]:
                new_list.append(point)
            else:
                new_list[-1] = [point[0], min(new_list[-1][1], point[1])]
        return len(new_list)


if __name__ == '__main__':
    solution = Solution()
    points = [[9, 12], [1, 10], [4, 11], [8, 12], [3, 9], [6, 9], [6, 7]]
    print(solution.findMinArrowShots(points))
