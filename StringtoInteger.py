#use ASCII value to refer the real value of a char
#notice edge cases
class Solution:
    # @return an integer
    def atoi(self, str):
        if str=='':
            return 0
        x=0
        flag=True
        start=False
        end=False
        while not (start == True and end == True):
            for i in xrange(len(str)):
                if start == False:
                    if ord(str[i])== 32:
                        ' '
                        continue
                    elif ord(str[i])== 43:
                        '+'
                        flag=True
                        start = True
                        try:
                            if not (ord(str[i+1])>=48 and ord(str[i+1])<=57):
                                return 0
                        except IndexError:
                            return 0
                        continue
                    elif ord(str[i])== 45:
                        '-'
                        flag=False
                        start = True
                        try:
                            if not (ord(str[i+1])>=48 and ord(str[i+1])<=57):
                                return 0
                        except IndexError:
                            return 0
                        continue
                    elif ord(str[i])>=48 and ord(str[i])<=57:
                        '0~9'
                        start = True
                        x=x*10+ord(str[i])-48
                        continue
                    else:
                        return 0
                if start == True and end == False:
                    if ord(str[i])>=48 and ord(str[i])<=57:                       
                        x=x*10+ord(str[i])-48
                    else:
                        end=True
            break
        if not flag:
            x=0-x
        if x>2147483647:
            return 2147483647
        if x<-2147483648:
            return -2147483648
        return x
