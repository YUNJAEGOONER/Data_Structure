def bubble_sort(array , n):
    for i in range(1, n):
        for j in range(1, n-1):
            if array[j-1] > array[j]:
                big = array[j-1]
                small = array[j]
                array[j] = big
                array[j-1] =small

    return array

array = [6,5,3,1,8]
n = len(array)
array = bubble_sort(array,len(array))
print(array)

