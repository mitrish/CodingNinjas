import sys
N = int(input())
a= [int(i) for i in input().split(" ") if len(i)>0]
 
for i in range(len(a)): 
    min_index = i
    for j in range(i+1, len(a)):
        if a[min_index] > a[j]:
            min_index = j     
    a[i], a[min_index] = a[min_index], a[i]
 

for i in range(len(a)):
    print(a[i],end = " ") 
