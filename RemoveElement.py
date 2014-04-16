'''
http://oj.leetcode.com/problems/remove-element/
'''

class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        n=0
        for i in xrange(len(A)):
            if not A[i]==elem:
                A[n]=A[i]
                n=n+1
        return n
