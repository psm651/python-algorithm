m, n = map(int,input().split())
l=[]
valList=[]

for f in range(m):
    l.append(input())

for a in range(m - 7):
    for b in range(n - 7):
        bFirst=0
        wFirst=0
        for i in range(a, a+8):
            for j in range(b, b+8):
                if (i+j)%2 == 0:
                    if l[i][j] != 'W':
                        wFirst += 1
                    elif l[i][j] != 'B':
                        bFirst += 1
                else:
                    if l[i][j] != 'B':
                        wFirst += 1
                    elif l[i][j] != 'W':
                        bFirst += 1
        valList.append(bFirst)
        valList.append(wFirst)
print(min(valList))
                    