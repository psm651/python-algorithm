val = int(input())
for i in range(0,val):
    stra=''
    strb=''
    for j in range(1,val+1):
        if j % 2 != 0:
            stra +='*'
        if j % 2 == 0:
            stra +=' '
    print(stra)
    if val > 1:
        for k in range(1,val+1):
            if k % 2 != 0:
                strb +=' '
            if k % 2 == 0:
                strb +='*'
        print(strb)
