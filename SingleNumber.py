class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        a=0
        for i in A:
            a=a^i
        return a
