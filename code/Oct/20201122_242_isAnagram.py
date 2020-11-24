class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_dict = {}
        for s_c, t_c in zip(s, t):
            char_dict[s_c] = char_dict.get(s_c, 0) + 1
            char_dict[t_c] = char_dict.get(t_c, 0) - 1
        for value in char_dict.values():
            if value != 0:
                return False
        return True


if __name__ == '__main__':
    solution = Solution()
    s = "anagram"
    t = "nagaram"
    print(solution.isAnagram(s, t))
