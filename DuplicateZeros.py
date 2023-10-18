def duplicateZeros(arr) -> None:
    i = 0
#    while i < len(arr)-1:
    for i in range(len(arr)- 1):
        if arr[i] == 0:
            arr.pop()
            arr.insert(i+1,0)
            i += 1
        i += 1
    print(arr)
arr1 = [9,0,2,3,0,4,5,0]
duplicateZeros(arr1)