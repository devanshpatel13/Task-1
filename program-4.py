n=int(input("how many alphabates you want to display ? "))

# for i in range(n):
# 	print(" "*(n-i+1),end ="")
#
# 	for j in range(i,0,-1):
# 		print(chr(65+j),end = "")
# 	#
# 	for j in range(i+1):
# 		print(chr(65+j),end = "")
#
# 	print("")


#
for i in range(n):
	print(" "*(n - i + 1), end="")

	for j in range(i,0,-1 ):
		print(chr(65 + j), end="")
	for j in range(i + 1):
		print(chr(65 + j), end="")

	print()


