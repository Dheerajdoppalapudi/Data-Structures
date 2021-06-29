# All pair shortest path (Floyd Warshall Algorithm)

def allpairshortestpath(arr):
    for k in range(len(arr)):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if i == j:
                    continue
                else:
                    arr[i][j] = min(arr[i][j], (arr[i][k]+arr[k][j]))
    return arr

INF = 97532
graph = [[0, 3, INF, 7],
         [8, 0, 2, INF],
         [5, INF, 0,   1],
         [2, INF, INF, 0]
         ]
fi = allpairshortestpath(graph)
print("Solution: ")
for i in fi:
    print(i)
