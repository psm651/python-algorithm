import sys
T = int(sys.stdin.readline())
def checkVPS(checkStr):
    print(checkStr.pop())

for _ in range(T):
    checkStr = list(sys.stdin.readline().rstrip())
    checkVPS(checkStr)