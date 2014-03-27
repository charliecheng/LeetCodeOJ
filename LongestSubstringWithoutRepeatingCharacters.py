class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        list=[]
        position=[]
        counter=0
        max=0
        i=0
        while i < len (s):
            #print i
            if not s[i] in list:
                counter=counter+1
                list.append(s[i])
                position.append(i)
                i=i+1
                #print list
                #print 'new'
                continue
            else:
                #print 'old'
                pos=position[list.index(s[i])]
                if counter>max:                   
                    max=counter
                i = pos+1
                counter=1
                list=[]
                position=[]
                list.append(s[i])
                position.append(i)
                i=i+1
                #print list
                continue
            
        if counter>max:
            max=counter
        return max   

if __name__=='__main__':
    a=Solution()
    print a.lengthOfLongestSubstring('qopubjguxhxdipfzwswybgfylqvjzhar')
