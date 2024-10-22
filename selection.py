def selection(arr):
    for i in range(len(arr)):
        index = i
        
        for j in range(i+1, len(arr)):
            if arr[j] < arr[index]:
                index = j
        
        arr[i], arr[index] = arr[index], arr[i]

arr = [33, 14, 54, 21, 30]
selection(arr)
print( arr)
