"""

퀵정렬
평균 시간복잡도 O(n * log n)
최악 시간복잡도 O(n*n)

"""
def quick_sort(arr):
    def recursive_arr_sort(low, high):
        if(low < high):
            mid = partion_sort(low, high)
            recursive_arr_sort(low, mid-1)
            recursive_arr_sort(mid, high)
        return arr

    def partion_sort(low, high):
        pivot = arr[(low + high) //2 ]
        while low <= high:
            while arr[low] < pivot:
                low += 1
            while arr[high] > pivot:
                high -= 1
            if low <= high:
                arr[low], arr[high] = arr[high], arr[low]
                low, high = low + 1, high - 1
        return low
    return recursive_arr_sort(0, len(arr)-1)


#def quick_sort(arr):
#    if len(arr) <= 1:
#        return arr
#    pivot = arr[len(arr) // 2]
#    lesser_arr, equal_arr, greater_arr = [], [], []
#    for num in arr:
#        if num < pivot:
#            lesser_arr.append(num)
#        elif num > pivot:
#            greater_arr.append(num)
#        else:
#            equal_arr.append(num)
#    return quick_sort(lesser_arr) + equal_arr + quick_sort(greater_arr)

arr = [6,1,2,5,8,4,3,10,9,7]
print(quick_sort(arr))
        
