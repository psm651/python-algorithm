string_arr= list()
compare_dic = {')':'(', ']':'['}

def check_couple(sentence):
    stack = []
    for j in range(len(sentence)):
        if sentence[j] == '(' or sentence[j] =='[':
            stack.append(sentence[j])
        elif sentence[j] == ')' or sentence[j] ==']':
            if not stack:
                return 'no'
            top = stack.pop()
            if top != compare_dic[sentence[j]]:
                return 'no'
    if not stack:
        return 'yes'
    else :
        return 'no'

#input받는 부분
line = ''
while True:
    line = input()
    if line =='.':
        break
    string_arr.append(line)

for i in range(len(string_arr)):
    print(check_couple(string_arr[i]))

