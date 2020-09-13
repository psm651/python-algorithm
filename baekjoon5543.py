buger_list=[]
drink_list=[]
for i in range(0,5):
    if i<3:
        buger_list.append(int(input()))
    else:
        drink_list.append(int(input()))
print(min(buger_list)+min(drink_list)-50)
