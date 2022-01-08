def quick_sort(array, l, r):
    if l < r:
        q = partition(array, l, r)
        print(q)
        quick_sort(array, l, q - 1)
        quick_sort(array, q + 1, r)
 
def partition(array, l, r):
    x = array[r]
    # i 为小于等于X区间的
    i = l - 1
    for j in range(l, r):
        if array[j] <= x:
            i += 1
            array[i], array[j] = array[j], array[i]
    array[i + 1], array[r] = array[r], array[i+1]
    return i + 1


if __name__ == "__main__":
	arr = [1,4,7,1,5,5,3,85,34,75,23,75,2,0]
	quick_sort(arr, 0, len(arr)-1)
	print(arr)
p,r 为数组的两端，不会变
