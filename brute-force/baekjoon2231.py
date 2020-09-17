#N = int(input())
#print_num = 0
#for i in range(1, N+1):
    #div_num = list(map(int, str(i)))
    #sum_num = i + sum(div_num)
    #if(sum_num == N):
        #print_num = i
        #break
#print(print_num)
N=int(input())
M=N-(9*len(str(N)))
M = 1 if M < 1 else M
result=[v for v in range(M,N+1) if sum(map(int,str(v)))+v == N]
print(result[0] if result else 0)