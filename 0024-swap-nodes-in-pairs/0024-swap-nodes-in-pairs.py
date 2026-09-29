class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0)
        dummy.next = head

        prev = dummy

        while prev.next and prev.next.next:

            first = prev.next
            second = first.next
            next_pair = second.next

            prev.next = second
            second.next = first
            first.next = next_pair

            prev = first

        return dummy.next