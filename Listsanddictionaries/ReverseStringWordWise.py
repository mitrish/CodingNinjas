word = input()
word2 = word.split()
N = len(word2)
for i in range(N-1,-1,-1):
    print(word2[i], end = " ")
