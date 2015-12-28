def insertion_sort(arr):
	for i in range(1, len(arr)):
		item = arr[i]
		position = i
		while position > 0 and arr[position-1] > item:
			arr[position] = arr[position-1]
			position -= 1

		arr[position] = item

	return arr