#write a  python sript to identify the duplicate values in the list and print the list of ony unique.....

num_1 = int(input(" enter numbers   "))
list_1 = []
diff_list = [] 
for i in range(num_1):
	Number = input("give the number:  ")
	list_1.append(Number)
for Number in list_1 :
	if Number not in diff_list :
		diff_list.append(Number)
print(diff_list)	