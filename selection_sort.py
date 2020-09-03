"""

선택정렬

"""


def selection_sort(arr):
    count=0
    for i in range(len(arr)-1):
        min_index = i
        for j in range(i+1, len(arr)):
            count += 1
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index],arr[i]
    print(arr,count)

selection_sort([1,2,5,4,3,9,8,6,10,7])
                
