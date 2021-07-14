import sys

N = int(sys.stdin.readline())
cnt = 0
result = N
while True:
    a = result // 10
    b = result % 10
    c = (a+b) % 10
    result = (b*10) + c
    cnt = cnt + 1
    if(result == N):
        break
print(cnt)