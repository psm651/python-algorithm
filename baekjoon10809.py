S = input()

for i in range(97,123):
    if S.find(chr(i)) != -1:
        print(S.index(chr(i)),end=' ')
    else:
        print(-1,end=' ')
