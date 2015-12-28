def merge_sort(arr):
	n = len(arr)
	if n>1:
		half = n//2
		A = arr[:half]
		B = arr[half:]
		C = arr
		print "splitting ", A, B
		merge_sort(A)
		merge_sort(B)

		i = 0
		j = 0
		k = 0

		#merge array A and B into the result array
		while i < len(A) and j < len(B):
			if A[i] < B[j]:
				C[k] = A[i]
				i = i+1
			else:
				C[k] = B[j]
				j = j+1
			k = k+1

		#insert left over elements in A into the result array
		while i < len(A):
			C[k] = A[i]
			i += 1
			k += 1

		#instert left over elements in B into the result array
		while j < len(B):
			C[k] = B[j]
			j += 1
			k += 1
		print "merging ",C
		return C
