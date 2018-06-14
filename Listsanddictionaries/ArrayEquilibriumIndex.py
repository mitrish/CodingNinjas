def equilibrium(arr,size):
    lsum = 0
    rsum = 0
    for i in range(size):
        lsum = 0
        rsum = 0
        for j in range(i+1,size):
            rsum += arr[j]
        for j in range(i):
            lsum += arr[j]
        if lsum == rsum:
            return i
     
    return -1
             
N = int(input())
arr = [int(i) for i in input().split(" ") if len(i)>0]
print(equilibrium(arr,N))
