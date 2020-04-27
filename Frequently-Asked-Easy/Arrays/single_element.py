
def singleNumber(nums):

    ref = {}
    for i in nums:
        if i not in ref:
            ref[i] = 1
        else:
            ref[i] +=1
    for k,v in ref.items():
        if v == 1:
            return k


                    #  a = 0
                    #  for i in nums:
                    #      a ^= i
                    # return a

