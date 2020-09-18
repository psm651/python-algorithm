jul = int(input())
total = []
for i in range(jul):
    val = int(input())
    if val == 0:
        total.pop()
    else:
        total.append(val)
print(sum(map(int,total)))
