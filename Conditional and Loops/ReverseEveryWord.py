word = input()
word2 = word.split(" ")
empty = ""
for i in word2:
	k = "".join(reversed(i))
	empty = empty + k + " "
    
print(empty.rstrip())
