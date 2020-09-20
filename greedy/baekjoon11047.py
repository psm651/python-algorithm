n, k = map(int,input().split())
coinList = []
coins = 0
for i in range(n):
    coinList.append(int(input()))
for j in range(len(coinList)-1, -1, -1):
    if coinList[j] > k:
        continue
    else:
        coins += (k//coinList[j])
        k = k%coinList[j]
print(coins)