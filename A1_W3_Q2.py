import heapq

def kLargest(arr, k):
    global Sum
    sum = 0
    # Sort the given array arr in reverse

    arr.sort(reverse=True)
    # Print the first kth largest elements
    for i in range(k):
         print(arr[i], end=" ")

def kthLargestSum(arr, n, k):
    # array to store  sums
    sum = []
    sum.append(0)
    sum.append(arr[0])
    for i in range(2, n + 1):
        sum.append(sum[i - 1] + arr[i - 1])

    # priority_queue of min heap
    Q = []
    heapq.heapify(Q)
    for i in range(1, n + 1):


        for j in range(i, n + 1):
            x = sum[j] - sum[i - 1]

            # if queue has less then k

            if len(Q) < k:
                heapq.heappush(Q, x)
            else:
                if Q[0] < x:
                    heapq.heappop(Q)
                    heapq.heappush(Q, x)

    return Q[0]



# calls the function to find out the


arr = [1, 23, 12, 9, 30, 2, 50, 60, 89]
n = len(arr)
k = 3
kLargest(arr, k)
# k-th largest sum
print(kthLargestSum(arr, n, k))

