class Solution:
    # @return an integer
    def __init__(self):
        self.dict={}
        self.dict['M']=1000
        self.dict['CM']=900
        self.dict['D']=500
        self.dict['CD']=400
        self.dict['C']=100
        self.dict['XC']=90
        self.dict['L']=50
        self.dict['XL']=40
        self.dict['X']=10
        self.dict['IX']=9
        self.dict['V']=5
        self.dict['IV']=4
        self.dict['I']=1
    def romanToInt(self, s):
        num=0
        i=0
        while not i==len(s):
            if s[i:].startswith('CM'):
                num=num+900
                i=i+2
            elif s[i:].startswith('CD'):
                num=num+400
                i=i+2
            elif s[i:].startswith('XC'):
                num=num+90
                i=i+2
            elif s[i:].startswith('XL'):
                num=num+40
                i=i+2
            elif s[i:].startswith('IX'):
                num=num+9
                i=i+2
            elif s[i:].startswith('IV'):
                num=num+4
                i=i+2
            else:
                num=num+self.dict[s[i]]
                i=i+1
        return num
