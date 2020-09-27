import sys
N=sys.stdin.readline().strip()
stackList=[]

def push(val):
    return stackList.append(val)
def pop():
    if len(stackList) == 0:
        return -1
    data = stackList[-1]
    del stackList[-1]
    return data
def size():
    return len(stackList)
def empty():
    if len(stackList)==0:
        return 1
    else:
        return 0
def top():
    if len(stackList) == 0:
        return -1
    return stackList[-1]

for i in range(int(N)):
    inputLine = sys.stdin.readline().strip().split()
    cmd = inputLine[0] 
    if cmd == 'push':
        push(int(inputLine[1]))
    elif cmd == 'pop':
        print(pop())
    elif cmd == 'size':
        print(size())
    elif cmd == 'empty':
        print(empty())
    elif cmd == 'top':
        print(top())


