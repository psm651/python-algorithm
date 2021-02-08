import sys, string

N = int(sys.stdin.readline())
for i in range(N):
    arr = list(map(int,sys.stdin.readline().split(' ')))
    students_count = arr[0]
    good_students = 0
    total = sum(arr[1:])
    avg = total/students_count
    for j in arr[1:]:
        if j > avg:
            good_students = good_students + 1
    result = good_students/students_count
    print("{0:.3f}".format(round(result*100,3))+'%')
    