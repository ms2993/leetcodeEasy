nums= [4,1,2,1,2]
def duplicate(nums):
    temp = []
    for i in nums:
        if i in temp:
            temp.remove(i)
        else:
            temp.append(i)
    return temp.pop()
print(duplicate(nums))



