"""

삽입정렬

"""

def insertion_sort(arr):
    for i in range(1,len(arr)):
        j=i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1],arr[j] = arr[j], arr[j-1]
            j -= 1

    print(arr)

arr = [1,10,9,5,8,2,7,6,4,3]
insertion_sort(arr)
