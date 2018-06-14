def printLeaders(arr,size):
    for i in range(0, size):
        for j in range(i+1, size):
            if arr[i]<=arr[j]:
                break
        if j == size-1: # If loop didn't break
            print(arr[i], end = " ")
 
n = int(input())
a = [int(i) for i in input().split(" ") if len(i)>0]

printLeaders(a, n)
