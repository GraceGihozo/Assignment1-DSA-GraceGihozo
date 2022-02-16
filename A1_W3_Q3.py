# Returns the maximum profit that
# can be put in a knapsack of
# capacity W
def Burglar_breaks(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Create table K[][] from the bottom up.
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1]
                              + K[i - 1][w - wt[i - 1]],
                              K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]
#Driver Code
val = [2500, 1700, 1200, 3000, 4100, 2000, 7000, 7500]
wt = [5, 3, 1, 6, 8, 4, 11, 12]
W = 20
n = len(val)
print(Burglar_breaks(W, wt, val, n))