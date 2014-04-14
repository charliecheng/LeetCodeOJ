class Solution:
    # @return a string
    def longestCommonPrefix(self, strs):
        if strs==[]:
            return ''
        lists=list(strs[0])
        for i in xrange(1,len(strs)):
            try:
                for j in xrange(len(lists)):
                    if not strs[i][j]==lists[j]:
                        lists=lists[0:j]
                        break
                
            except IndexError:
                lists=lists[0:j]
        return ''.join(lists)
