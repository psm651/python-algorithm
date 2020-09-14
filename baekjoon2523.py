val = int(input())
for i in range(1,val+1):
    print('*'*i,end="\n")
for j in range(val-1, 0, -1):
    print('*'*j,end="\n")