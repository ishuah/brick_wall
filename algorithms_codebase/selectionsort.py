def selection_sort(arr):
	for i in range(len(arr)):
		value = arr[i]
		pointer = 0
		for j in range(i+1, len(arr)):
			if arr[j] < value:
				value = arr[j]
				pointer = j
		if pointer:
			arr[pointer] = arr[i]
			arr[i] = value
	return arr
