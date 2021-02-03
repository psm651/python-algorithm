import sys
N = int(sys.stdin.readline())

str=''
for i in range(N-1, -1, -1):
    str = ' ' * i + '*' * (N-i)
    print(str)