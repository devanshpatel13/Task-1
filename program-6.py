def pushZerosToEnd(list1, n):
	count = 0 
	
	for i in range(n):
		if list1[i] != 0:
			list1[count] = list1[i]
			print(list1[count],"fffffffffffffff")
			count+=1
	
	while count < n:
		list1[count] = 0
		print(list1[count], "ddddddddddddddddd")

		count += 1
		
list1 = list() 

num = input("How many elements do you want: ") 
for i in range(int(num)): 
    n = input("Enter a value: ") 
    list1.append(int(n))
print(list1)


n = len(list1)
pushZerosToEnd(list1, n)
print("Array after pushing all zeros to end of array:")
print(list1)



