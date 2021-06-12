You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 

Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.

---------------------Recursion----------------------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:        
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def helper(l1, l2, pass_val):
            if l1 is None and l2 is None and pass_val < 1:
                return
            
            l1_next, l1_val, l2_next, l2_val = None, 0, None, 0
            
            if l1 is not None:
                l1_next = l1.next
                l1_val = l1.val
            
            if l2 is not None:
                l2_next = l2.next
                l2_val = l2.val
            

            s = l1_val + l2_val + pass_val
            pass_val = s // 10
            s = s % 10
            
            return ListNode(val=s, next=helper(l1_next, l2_next, pass_val))
        
        return helper(l1, l2, 0)

