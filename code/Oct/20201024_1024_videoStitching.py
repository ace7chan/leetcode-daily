from typing import List


class Solution:
    def videoStitching(self, clips: List[List[int]], T: int) -> int:
        clips = sorted(clips, key=lambda key: (key[0], key[1]))
        if clips[-1][1] < T or clips[0][0] > 0:
            return -1
        final_list = [clips[0]]
        for cur_clip in clips[1:]:
            if final_list[-1][1] >= T:
                break
            # 1. 如果包裹住前面的, 则不断去除
            while len(final_list) > 0 and cur_clip[1] >= final_list[-1][1] and cur_clip[0] <= final_list[-1][0]:
                final_list.pop()
            while len(final_list) > 1 and cur_clip[1] >= final_list[-1][1] and cur_clip[0] <= final_list[-2][1]:
                final_list.pop()
            # 2. 当前栈为空, 直接加进去
            if len(final_list) == 0:
                final_list.append(cur_clip)
            # 3. 出现断层, 直接跳出
            elif cur_clip[0] > final_list[-1][1]:
                return -1
            # 4. 当前处于被包裹阶段
            elif cur_clip[1] <= final_list[-1][1]:
                continue
            else:
                final_list.append(cur_clip)
        return len(final_list)


if __name__ == '__main__':
    solution = Solution()
    clips = [[8, 20], [4, 23], [10, 14], [3, 25], [0, 24], [5, 18], [8, 15], [9, 23]]
    clips = sorted(clips, key=lambda key: (key[0], key[1]))
    print(clips)
    print(solution.videoStitching(clips, 6))
