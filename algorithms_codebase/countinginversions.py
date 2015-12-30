def merge_and_count_split_inv(A):
	if len(A) > 1:
		half = len(A)//2
		B = A[:half]
		C = A[half:]
		D = A

		merge_and_count_split_inv(B)
		merge_and_count_split_inv(C)

		i = 0
		j = 0
		k = 0
		count = 0

		while i < len(B) and j < len(C):
			if B[i] < C[j]:
				D[k] = B[i]
				k +=1
				i +=1
			else:
				D[k] = C[j]
				j += 1
				k += 1
				count += len(B) - i

		return count
