l = [7,1,5,3,6,4]
def sell(l):
    max = 0
    profit = 0
    ll = len(l)
    for i in range(ll):
        for j in range(i+1,ll):
            profit = l[i]-l[j]
            if max < profit:
                max = profit
    return max
print("maximum profit:",sell(l))

    

