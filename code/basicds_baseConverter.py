def baseConverter(num, base):
	digits = "0123456789ABCDEF"
	s = []
	while num > 0:
		s.append(num % base)
		num = num // base
	binaryStr = ""
	while s != []:
		binaryStr += digits[s.pop()]
	return binaryStr