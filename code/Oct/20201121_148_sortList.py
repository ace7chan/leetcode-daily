from typing import List


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        res = head
        if head is None or head.next is None:
            return res
        next = head.next
        head.next = None
        head = next
        while head:
            cur = head
            next = head.next
            head.next = None
            head = next
            start = res
            if start.val >= cur.val:
                cur.next = start
                res = cur
            else:
                while start.next and start.next.val < cur.val:
                    start = start.next
                next = start.next
                start.next = cur
                cur.next = next
        return res


if __name__ == '__main__':
    solution = Solution()
    n1 = ListNode(4)
    n2 = ListNode(2)
    n3 = ListNode(1)
    n4 = ListNode(3)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    res = solution.sortList(n1)
    while res:
        print(res.val)
        res = res.next
