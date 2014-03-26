class Solution:
    # @return a float
    '''
    It is said that it is better not to use recursion in python.
    Only 1000 times recursion is allowed
    '''
    def findMedianSortedArrays(self, A, B):
        m=len(A)
        n=len(B)
        if (m+n)%2==1:
            return float(self.findKthSmallest(A, m, B, n, (m+n+1)/2))
        else:
            a=float(self.findKthSmallest(A, m, B, n, (m+n)/2))
            b=float(self.findKthSmallest(A, m, B, n, (m+n+2)/2))
            return (a+b)/2
        return
    def findKthSmallest(self,A,m,B,n,k):
        if m>n:
            return self.findKthSmallest(B, n, A, m, k)
        if m==0:
            return B[k-1]
        if k==1:
            if A[0]>B[0]:
                return B[0]
            else:
                return A[0]
        if k/2<m:
            i=k/2
        else:
            i=m
        j=k-i
        if A[i-1]<B[j-1]:
            return self.findKthSmallest(A[i:m+1], m-i, B[0:j], j, k-i)
        elif A[i-1]>B[j-1]:
            return self.findKthSmallest(A[0:i], i, B[j:n+1], n-j, k-j)
        else:
            return A[i-1]
            
        #Edge cases is extremely difficult to consider.
        #Thus, need to find right place to start divide-conquer algorithm, which is the value of i an j.
        #First find the Kth smalest in two sorted arrays.
