val = int(input())
for i in range(val):
    print(' ' * i+'*' * ((val-i)*2-1))
for j in range(1,val):
    print(' ' * (val-j-1)+'*' * (j*2+1))