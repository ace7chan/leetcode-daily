class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        rd_num = {'R': 0, 'D': 0}
        for c in senate:
            rd_num[c] += 1
        idx = 0
        flag = [True] * len(senate)
        flag_r, flag_d = 0, 0
        while True:
            if rd_num['R'] == 0:
                return 'Dire'
            elif rd_num['D'] == 0:
                return 'Radiant'
            if flag[idx]:
                if senate[idx] == 'R':
                    if flag_d > 0:
                        flag[idx] = False
                        rd_num['R'] -= 1
                        flag_d -= 1
                    else:
                        flag_r += 1
                else:
                    if flag_r > 0:
                        flag[idx] = False
                        rd_num['D'] -= 1
                        flag_r -= 1
                    else:
                        flag_d += 1
            idx += 1
            idx = idx % len(senate)


if __name__ == '__main__':
    solution = Solution()
    print(solution.predictPartyVictory("RDD"))
