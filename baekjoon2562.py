arr=list()
for i in range(9):
    arr.append(int(input()))
maxValue = max(arr)
print(maxValue)
print(int(arr.index(maxValue))+1)
