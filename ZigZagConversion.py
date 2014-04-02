'''
#The algorithom is quite simple, but it took much longer time to be accepted than I expected.
#The first few version always trigger TLE. The problem is that I used a extra dictionary at first. 
Moreover, it is very slow to use string + string to create new string. 
It is better to use ''.join from list to create a new string. It is easy, cos in python the string content cannot be manipulated.
xrange() is faster than range()
For more information:
http://www.skymind.com/~ocrow/python_string/
'''
class Solution:
    # @return a string
    def convert(self, s, nRows):
        if nRows==1:
            return s
        newString=[[] for _ in xrange(nRows)]
        #dict={}
        para=2*nRows-2
        for i in xrange(len(s)):
            
            #i=a*(2*nRows-2)+b
            b=i%para
            if b <nRows:
                newString[b].append(s[i])
            else:
                newString[para-b].append(s[i])
        #print dict
        #for b in dict.keys():
           #while not dict[b]==[]:
               #newString=newString+dict[b].pop(0)
            #newString.extend(dict[b])   
        return  ''.join(''.join(row) for row in newString)
    
if __name__=='__main__':
    a=Solution()
    print a.convert("PAYPALISHIRING", 3)
