def bubble_sort(arr):
	for numpass in range(len(arr)-1, 0, -1):
		for i in range(numpass):
			if arr[i+1] < arr[i]:
				temp = arr[i]
				arr[i] = arr[i+1]
				arr[i+1] = temp
	return arr