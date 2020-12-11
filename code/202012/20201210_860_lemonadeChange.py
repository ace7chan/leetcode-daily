from typing import List


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_dict = {5: 0, 10: 0}
        for bill in bills:
            if bill == 5:
                bill_dict[bill] += 1
            elif bill == 10:
                if bill_dict[5] == 0:
                    return False
                bill_dict[5] -= 1
                bill_dict[10] += 1
            else:
                if bill_dict[5] == 0:
                    return False
                bill_dict[5] -= 1
                if bill_dict[10] > 0:
                    bill_dict[10] -= 1
                    continue
                elif bill_dict[5] >= 2:
                    bill_dict[5] -= 2
                else:
                    return False
        return True


if __name__ == '__main__':
    solution = Solution()
    print(solution.lemonadeChange([5, 5, 5, 10, 5, 5, 10, 20, 20, 20]))
