"""

버블정렬

"""

def bubble_sort(arr):
    count=0
    for i in range(len(arr)-1):
        for j in range(0, len(arr)-i-1):
            count +=1
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    print(arr, count)
    
# 최적화 버블정렬 : 중간 불필요 스왑 건너뛰고 다음 스왑자리로 이동
def optimize_bubble_sort(arr):
    count = 0
    end = len(arr) - 1
    while end > 0:
        last_swap = 0
        for i in range(end):
            count +=1
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                last_swap = i
        end = last_swap
    print(arr, count)

arr_list=[1,9,5,8,6,7,4,3,2,10]
bubble_sort(arr_list)
