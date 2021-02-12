import sys

N = int(sys.stdin.readline())

for i in range(N):
    accrued_count=1
    result = 0
    line = map(str,sys.stdin.readline().rstrip())
    for j in line:
        if j == 'O':
            result = result + accrued_count
            accrued_count = accrued_count + 1
        elif j == 'X':
            accrued_count = 1
    print(result)