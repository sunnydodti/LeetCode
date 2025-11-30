class Solution:
    def removeNthFromEnd(self, head, n: int):

        if not head.next:
            return head.next

        curr = head
        l = 0
        while curr:
            l += 1
            curr = curr.next

        target = l - n
        print(n, l, target)
        print(head)

        curr = head
        i = 1

        if target == 0:
            return curr.next

        while i <= target:
            if i == target:
                curr.next = curr.next.next
            curr = curr.next
            i += 1

        return head
