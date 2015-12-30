def merge_and_count_split_inv(A):
	if len(A) > 1:
		half = len(A)//2
		B = A[:half]
		C = A[half:]

		merge_and_count_split_inv(B)
		merge_and_count_split_inv(C)

		i = 0
		j = 0
		k = 0
		count = 0

		while i < len(B) and j < len(C):
			if B[i] < C[j]:
				A[k] = B[i]
				k +=1
				i +=1
			else:
				A[k] = C[j]
				j += 1
				k += 1
				count += len(B) - i

		while i < len(B):
			A[k] = B[i]
			k +=1
			i +=1
		while j < len(C):
			A[k] = C[j]
			k+=1
			j+=1

		return count
