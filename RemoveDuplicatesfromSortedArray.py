'''
http://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/
remove will trigger TLE
'''
class Solution:
    # @param a list of integers
    # @return an integer
    def removeDuplicates(self, A):
        i=0
        j=1
        if A==[]:
            return 0
        a=A[0]
        length=1
        while True:
            try:
                i=i+1
                if A[i]==A[i-1]:
                    continue
                else:
                    A[j]=A[i]
                    j=j+1
                    length=length+1
            except IndexError:
                #print A
                return length
if __name__=='__main__':
    a=Solution()
    A=[1,1,1,1,2,2,2,3,3,4,4,4]
    print a.removeDuplicates(A)
