# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None:
            return head
        first = head
        second = head.next
        first_node = first
        second_node = second
        while first is not None and first.next is not None:
            if first.next.next is None:
                break
            first.next = second.next
            first = first.next
            second.next = first.next
            second = second.next
        first.next = second_node
        return first_node


if __name__ == '__main__':
    solution = Solution()
    a1, a2 = ListNode(1), ListNode(2)
    a3, a4 = ListNode(3), ListNode(4)
    # a5 = ListNode(5)
    a1.next = a2
    a2.next = a3
    a3.next = a4
    # a4.next = a5
    res = solution.oddEvenList(a1)
    while res:
        print(res.val)
        res = res.next
