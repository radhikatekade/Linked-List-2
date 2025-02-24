# Time complexity - O(max(m, n))
# Space complexity - O(1)

# Approach - Compute len(A) and len(B), reduce the length of longer LL to make it equal to length of shorter
# LL. Run the loop again till head(A) coincides with head(B).

from typing import Optional
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        if headA == None or headB == None:
            return None
        
        lenA = 0
        lenB = 0
        curr = headA
        while curr != None:
            lenA += 1
            curr = curr.next
        
        curr = headB
        while curr != None:
            lenB += 1
            curr = curr.next
        
        while lenA > lenB:
            headA = headA.next
            lenA -= 1

        while lenA < lenB:
            headB = headB.next
            lenB -= 1
        
        while headA != headB:
            headA = headA.next
            headB = headB.next
        
        return headA