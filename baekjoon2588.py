input1 =  input()
input2 =  input()
a_arr = [int(x) for x in str(input1)]
a_arr.reverse()
b_arr = [int(x) for x in str(input2)]
b_arr.reverse()
total_sum=0
for i in range(len(b_arr)):
    sum=0
    for j in range(len(a_arr)):
        #print(j)
        sum += a_arr[j]*pow(10,j) * b_arr[i]*pow(10,i)
    print(sum // pow(10,i))
    total_sum += sum
print(total_sum)

