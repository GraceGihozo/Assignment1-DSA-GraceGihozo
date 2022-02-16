# function to find the element with an odd number of occurrences
def Odd(a, a_size):
    for i in range(0, a_size):
        count = 0
        for j in range(0, a_size):
            if a[i] == a[j]:
                count += 1
        # If count of element is odd we return True and false
        if (count % 2 != 0):
            return a[i] and True

        else:
            if (count % 2 == 0):
                return False


# driver code
a = [2, 3, 5, 4, 5, 2, 4, 5, 2, 4, 2 , 2, 1]
n = len(a)
print(Odd(a, n))
