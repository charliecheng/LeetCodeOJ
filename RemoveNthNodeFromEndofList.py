'''
http://oj.leetcode.com/problems/remove-nth-node-from-end-of-list/
'''
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @return a ListNode
    def removeNthFromEnd(self, head, n):
        if head.next==None and n==1:
            return None
        dict={}
        i=1
        dict[1]=head
        node=head.next
        while not node == None:
            i=i+1
            dict[i]=node
            node=node.next
            
        if n==i:
            return dict[2]
        if n==1:
            dict[i-1].next=None
            return dict[1]
        dict[i-n].next=dict[i-n+2]
        return dict[1]

if __name__=='__main__':
    a1=ListNode(1)
    a2=ListNode(2)
    a3=ListNode(3)
    a4=ListNode(4)
    a1.next=a2
    a2.next=a3
    a3.next=a4
    a=Solution()
    x=a.removeNthFromEnd(a1, 3)
    while not x== None:
        print x.val
        x=x.next
