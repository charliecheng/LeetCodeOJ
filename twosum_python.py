class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        hash_table={}
        index = 0
        position={}
        for i in num:
            if 2*i==target:
                if i in hash_table.keys():
                    return (position[i]+1,index+1)
            hash_table[i]=i
            position[i]=index
            index=index+1
        for i in num:
            try:
                if hash_table[target-i] in hash_table.values():
                    if 2*i==target:
                        continue
                    else:
                        return (position[i]+1,position[target-i]+1)
            except KeyError:
                continue
                

        # Cases need to be considered:
        # [3,2,4] 6, [0,2,3,0],0
        # Thus need at least 2 hash tables to store both values and index
