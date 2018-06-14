N = int(input())
k,prevj,j = 1,1,1
for i in range(1,N+1):
  k = 2*prevj+i-1
  while(j < prevj + 1):
    if(i%2 != 0):
      print(k,end=" ")
    if(i%2 == 0):
      print(k-j)
    j += 1
  prevj = j
  
