import sys
data=sys.stdin.readline().rstrip().split('-')
result=0

for i in range(len(data)):
    su = data[i].split('+')
    for j in range(len(su)):
        if i==0:
            result += int(su[j])
        else :
            result -= int(su[j])
print(result)