def merge_and_count_split_inv(A):
	if len(A) > 1:
		half = len(A)//2
		B = A[:half]
		C = A[half:]
		count = 0
		leftcount = merge_and_count_split_inv(B)
		rightcount = merge_and_count_split_inv(C)

		i = 0
		j = 0
		k = 0
		

		while i < len(B) and j < len(C):
			if B[i] < C[j]:
				A[k] = B[i]
				k +=1
				i +=1
			else:
				A[k] = C[j]
				j += 1
				k += 1
				#print "split inversion ", len(B) - i
				count += len(B) - i

		while i < len(B):
			A[k] = B[i]
			k +=1
			i +=1
		while j < len(C):
			A[k] = C[j]
			k+=1
			j+=1

		count = count + leftcount + rightcount
		#print "count, merging ",count,A
		return count
	return 0