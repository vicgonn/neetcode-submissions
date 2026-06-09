# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        dummy = ListNode()
        tail = dummy

        if not l1:
            return l2
        elif not l2:
            return l1

        carry = 0
        while l1 and l2:
            calc = l1.val + l2.val
            result = calc + carry
            rem = result % 10
            div = result // 10
            carry = div

            # print(rem)
            # print(div)

            tempNode = ListNode(rem)
            tail.next = tempNode
            tail = tail.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        while l1:

            calc = l1.val + 0
            result = calc + carry
            rem = result % 10
            div = result // 10
            carry = div

            # print(rem)
            # print(div)

            tempNode = ListNode(rem)
            tail.next = tempNode
            tail = tail.next
            
            if l1:
                l1 = l1.next


        while l2:
            calc = l2.val + 0
            result = calc + carry
            rem = result % 10
            div = result // 10
            carry = div

            # print(rem)
            # print(div)

            tempNode = ListNode(rem)
            tail.next = tempNode
            tail = tail.next
            
            if l2:
                l2 = l2.next


        if carry:
            tempNode = ListNode(carry)
            tail.next = tempNode
            tail = tail.next
        
        return dummy.next