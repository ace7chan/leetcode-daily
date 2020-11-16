from typing import List


class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        people = sorted(people, key=lambda key: (key[0], -key[1]))
        res = []
        for p in people[::-1]:
            res.insert(p[1], p)
        return res


if __name__ == '__main__':
    solution = Solution()
    people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]
    print(solution.reconstructQueue(people))
