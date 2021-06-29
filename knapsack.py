def knapsack(profits, weigths, maxw):
    ratio = []
    for i in range(len(profits)):
        ratio.append(profits[i] / weigths[i])

    maxprofit = 0

    while True:
        maxi = max(ratio)
        indi = ratio.index(maxi)
        if maxw > 0:
            maxw = maxw - weigths[indi]
            if maxw > 0:
                maxprofit = maxprofit + profits[indi]
                profits.remove(profits[indi])
                weigths.remove(weigths[indi])
                ratio.remove(maxi)
            else:
                maxw = maxw + weigths[indi]
                maxprofit = maxprofit + (maxw / weigths[indi]) * profits[indi]
                break

    print(maxprofit)

knapsack([2, 3, 4, 5], [3, 4, 5, 6], 5)