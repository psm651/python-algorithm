a=int(input())
val = 1
def factorial(a):
    if a == 0 or a == 1:
        return 1
    return a * factorial(a-1)
print(factorial(a))
