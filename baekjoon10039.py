score_list = []
total_score = 0
for i in range(0,5):
    score_list.append(int(input()))
for j in range(len(score_list)):
    if score_list[j] < 40:
        total_score += 40
    else:
        total_score += score_list[j]
print(total_score//5) 


