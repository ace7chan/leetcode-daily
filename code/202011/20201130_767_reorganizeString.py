class Solution:
    def reorganizeString(self, S: str) -> str:
        cnt_dict = dict()
        for c in S:
            cnt_dict[c] = cnt_dict.get(c, 0) + 1
        S = [k * v for k, v in sorted(cnt_dict.items(), key=lambda k: -k[1])]
        S = ''.join(S)
        half_idx = (len(S) - 1) // 2
        left_idx, right_idx = 0, half_idx + 1
        res = []
        while left_idx <= half_idx and right_idx < len(S):
            if S[left_idx] == S[right_idx]:
                return ""
            res.append(S[left_idx])
            res.append(S[right_idx])
            left_idx += 1
            right_idx += 1
        if len(res) < len(S):
            res.append(S[left_idx])
        return "".join(res)


if __name__ == '__main__':
    solution = Solution()
    S = "vvvlo"
    print(solution.reorganizeString(S))
