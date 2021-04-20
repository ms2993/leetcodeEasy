l = [-2,1,-3,4,-1,2,1,-5,4]
def subarrayr(l):
    sumvalue = 0
    maxvalue = l[0]
    for i in l:
        if sumvalue < 0:
            sumvalue = 0
        sumvalue+=i
        maxvalue = max(sumvalue, maxvalue)            
    return maxvalue
print(subarrayr(l))