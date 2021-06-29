def jobsheduling(p, t):
    dict = {}
    for i in range(len(p)):
        dict[p[i]] = t[i]
    sor = sorted(dict.items(), reverse=True)
    newdict = {}
    for i in sor:
        newdict[i[0]] = i[1]
    #print("newdict", newdict)
    ma = max(t)
    ki = [-1] * (ma)
    for i in newdict:
        na = newdict[i]
        if ki[na - 1] == -1:
            ki[na - 1] = i
        else:
            for j in range(na - 1):
                if ki[j] == -1:
                    ki[j] = i
                    break
                else:
                    continue
    return ki


ti = [2,1,3,2,1]
profit = [60,100,20,40,20]
arr = jobsheduling(profit, ti)
arr = list(set(arr))
sum = 0
for i in arr:
    if i == -1:
        arr.remove(-1)
        break
    sum = sum + i
print(sum)
print(arr)
