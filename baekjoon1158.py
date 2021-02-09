import sys

N,M = map(int,sys.stdin.readline().split())
group = []
result = []
for i in range(N):
    group.append(i+1)

pop_num = 0
while len(group) > 0:
    pop_num = (pop_num + (M -1) ) % len(group)
    pop_value = group.pop(pop_num)
    result.append(str(pop_value))

print("<%s>" %(', '.join(result)))

