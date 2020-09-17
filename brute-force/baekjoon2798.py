N, M = map(int,input().split())
card_list = list(map(int,input().split()))
max_value = 0
for i in range(N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            current_value = card_list[i]+card_list[j]+card_list[k]
            if max_value < current_value and current_value <= M:
                max_value = current_value
print(max_value)