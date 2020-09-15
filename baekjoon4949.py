string_arr= list(input().split('.'))
stack = []
compare_dic = {')':'(', ']':'['}

print('------------------------------------')
print(string_arr[0])
for i in range(len(string_arr)):
    sentence = list(string_arr[i])
    for j in range(len(sentence)):
        if sentence[j] == '(' or sentence[j] =='[':
            stack.append(sentence[j])
        elif sentence[j] == ')' or sentence[j] ==']':
            top = stack.pop()
            if top != compare_dic[sentence[j]]:
                #print('no')
                break
    if len(stack) != 0:
        pass
        #print('no')
    else :
        pass
        #print('yes')