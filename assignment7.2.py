num=(1,2,3,4,5,6,7,8,9,10,11,12)
countodd=0
counteven=0
for x in num:
	if x % 2:
		counteven+=1
		else:
			countodd+=1
print("Number of even numbers",counteven)
print("Number of odd numbers",countodd)