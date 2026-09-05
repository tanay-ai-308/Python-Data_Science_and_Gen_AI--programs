def ChkPrime(No) :

	if (No<=1) :
		return 0
	else :
		for i in range (2,No,1) :
			if (No%i == 0) :
				return 0

		return 1