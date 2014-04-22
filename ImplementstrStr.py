'''
http://oj.leetcode.com/problems/implement-strstr/
Optimized Brute-Forced
'''

class Solution:
    # @param haystack, a string
    # @param needle, a string
    # @return a string or None
    def strStr(self, haystack, needle):
        if len(needle)>len(haystack):
            return None
        if needle=='':
            return haystack
        if haystack=='':
            return None
        len_haystack=len(haystack)
        len_needle=len(needle)
        for i in xrange(len_haystack-len_needle+1):
            if haystack[i:i+len_needle]==needle:
                return haystack[i:]
        return None

if __name__=='__main__':
    a=Solution()
    print a.strStr('','ss')
