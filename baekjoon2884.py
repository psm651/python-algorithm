a,b = map(int,input().split())
if b<45:
    b+=60
    a-=1
    if a<0:
        a=23
print(a,b-45)
