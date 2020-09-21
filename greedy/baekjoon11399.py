n=int(input())
userList=list(map(int,input().split()))
resultList=[]
result=0
userList.sort()

for j in range(len(userList)):
    result += userList[j]
    resultList.append(result)
print(sum(resultList))
