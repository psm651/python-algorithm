n = int(input())

def recursivFunc(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else :
        return recursivFunc(n-1) + recursivFunc(n-2)

print(recursivFunc(n))