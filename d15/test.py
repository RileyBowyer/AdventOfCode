arr = [131, 673, 234, 103, 18, 201, 96, 342, 965, 150, 630, 803,
       746, 422, 111, 537, 699, 497, 121, 956, 805, 732, 524, 37, 331]
rows = 5
columns = 5
length = len(arr)
l = range(length)
firstColumn = l[5::rows]
firstRow = range(1, columns)
for idx, val in enumerate(arr):
    if idx == 0:  # Targets first list value
        val == val  # Leaves first value the same
    if idx in firstRow:  # Targets values in first row after first value
        arr[idx] = arr[idx] + arr[idx-1]  # Adds all values in first row to the previous list value
    if idx in firstColumn:  # Targets all values in first column
        arr[idx] = arr[idx] + arr[idx-rows]  # adds value to the value above in previous row
    if idx not in firstColumn and idx not in firstRow:  # targes any other values not in first row or first column
        if arr[idx] + arr[idx-1] < arr[idx] + arr[idx-rows]:  # determine if value above or previous is smaller
            arr[idx] = arr[idx] + arr[idx-1]  # sets value
        else:
            arr[idx] = arr[idx] + arr[idx-rows]  # sets value
print(arr[-1])  # returns list