import sys
n = int(input())
mettingList = []

for i in range(n):
    a, b = map(int,sys.stdin.readline().split())
    mettingList.append((a, b))
mettingList.sort(key=lambda x: x[1])

def getMaxMettingCount():
    maxTotal = 0
    last = 0 
    for j in range(len(mettingList)):
        if last <= mettingList[j][0]:
            last = mettingList[j][1]
            maxTotal += 1
    return maxTotal
print(getMaxMettingCount())
        


            
        

# def getMaxMettingCount():
#     mettingCountList = []
#     diffVal=-1
#     for j in range(len(mettingList)):
#         if diffVal == mettingList[j][0]:
#             continue
#         diffVal = mettingList[j][0]
#         curCount = 0
#         for k in range(j+1,len(mettingList)):
#             if mettingList[j][1] > mettingList[k][0]:
#                 continue
#             else:
#                 curCount += 1
#                 break
#         mettingCountList.append(curCount)
#     return max(mettingCountList)

#print(getMaxMettingCount())

'''
[(0, 6), (1, 4), (2, 13), (3, 5), (3, 8), (5, 7), (5, 9), (6, 10), (8, 11), (8, 12), (12, 14)]
'''