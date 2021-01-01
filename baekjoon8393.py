import sys
num = int(sys.stdin.readline().rstrip())
result = 0
for i in range(num+1):
    result = result + i
print(result)
