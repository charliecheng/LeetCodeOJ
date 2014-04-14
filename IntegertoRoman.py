class Solution:
    # @return a string
    def __init__(self):
        self.dict={}
        self.dict[1000]='M'
        self.dict[900]='CM'
        self.dict[500]='D'
        self.dict[400]='CD'
        self.dict[100]='C'
        self.dict[90]='XC'
        self.dict[50]='L'
        self.dict[40]='XL'
        self.dict[10]='X'
        self.dict[9]='IX'
        self.dict[5]='V'
        self.dict[4]='IV'
        self.dict[1]='I'
        self.keys=[1000,900,500,400,100,90,50,40,10,9,5,4,1]
    def intToRoman(self, num):
        list=[]
        while not num == 0:
            for key in self.keys:
                if num>=key:
                    list.append(self.dict[key])
                    num=num-key
                    break

        return ''.join(list)
