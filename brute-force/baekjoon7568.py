su = int(input())
people = []
result = []
#무게, 키 순으로 정렬
for i in range(su):
    val = list(map(int,input().split()))
    people.append(val)
    result.append(1)
for j in range(len(people)):
    for k in range(j+1,len(people)):
        if people[j][0] > people[k][0] and people[j][1] > people[k][1]:
            result[k]+=1
        elif people[j][0] < people[k][0] and people[j][1] < people[k][1]:
            result[j]+=1
for a in range(len(result)):
    print(result[a], end=' ')