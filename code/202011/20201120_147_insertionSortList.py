# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        start = ListNode(-1)
        start.next = head
        cur = head.next
        head.next = None
        while cur:
            prev = start
            while prev.next and cur.val > prev.next.val:
                prev = prev.next
            cur_temp = cur
            cur = cur.next
            next = prev.next
            prev.next = cur_temp
            cur_temp.next = next
        return start.next


if __name__ == '__main__':
    solution = Solution()
    a1, a2 = ListNode(4), ListNode(2)
    a3, a4 = ListNode(1), ListNode(3)
    a1.next = a2
    a2.next = a3
    a3.next = a4
    res = solution.insertionSortList(a1)
    while res:
        print(res.val)
        res = res.next
