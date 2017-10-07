# coding = utf-8
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):# @return a ListNode
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        root = n = ListNode(0)
        while l1 or l2 or carry:
            v1 = v2 = 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, val = divmod(v1+v2+carry, 10)
            n.next = ListNode(val)
            n = n.next
        return root.next
        

def Create_ListNode(nums):
    _next = None
    for num in nums[::-1]:
        l1 = ListNode(num)
        l1.next = _next
        _next = l1
    return l1

s = Solution()
result = s.addTwoNumbers(Create_ListNode([2,4,3]), Create_ListNode([5,6,4]))
num = 0
while True:
    num = num *10 + result.val
    if result.next:
        result = result.next
    else:
        break
print num