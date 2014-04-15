'''
http://oj.leetcode.com/problems/merge-k-sorted-lists/
'''
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    def mergeKLists(self, lists):
        while None in lists:
            lists.remove(None)
        if lists==[]:
            return None
        templist=[]
        for i in lists:
            node=i
            while not node==None:
                templist.append(node.val)
                node=node.next
        templist.sort()
        nodelist=[]
        for i in xrange(len(templist)):
            tempnode=ListNode(templist[i])
            nodelist.append(tempnode)
        if len(nodelist)==1:
            return nodelist[0]
        for i in xrange(len(nodelist)-1):
            nodelist[i].next=nodelist[i+1]
        return nodelist[0]
