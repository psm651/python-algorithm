import sys
N=int(sys.stdin.readline().rstrip())

for i in range(N):
    a, b=map(int,sys.stdin.readline().split())
    print('Case #'+str(i+1)+': '+str(a+b))
