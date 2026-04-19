"""a=45
print(type(a),(a))
f_name = "nitya"
l_name = "jain"
print("my name firest name is {} and my last name is {}".format (f_name ,l_name))
#fomat is a sting formating method ...
#conditions 
if(condition):
      contition ke hisab se exicute kar vana ha   
number= int(input("enter a number "))
num_2 = int(input ("enter num_2 "))
if(number%number==0 , number%num_2!=0):
	print("number is a prime number ")


n=int(input(" enter number of people: "))
sum = 0 
for i in range (n):
  	wight = int(input("enter wight: "))
  	sum = sum + wight
  	avergae_wight = sum/n 
print("avg wight",avergae_wight)"""


"""n_person=int(input("enter no. people: "))
sum = 0
for i in range (n_person):
	wieght = int (input("enter wieght :"))
	sum = sum + wieght

	number_person=4
	avergae_wight = sum/number_person 
	if (avergae_wight<=50):
		avergae_wight = sum/number_person
		print("use the lift: ")
print(avergae_wight)		
"""
"""n_lift=int(input("enter number of people : "))

list_1=[]
for i in range (1,n_lift+1):
        weight= int(input("enter wieght : "))
        list_1.append(weight)
print(list_1)
sum_1 = 0
for j in list_1:
	sum_1 = sum(list_1)
	if sum_1<300:
		print("lift all can be use the lift ")
	elif(sum_1>300):	
		print("you cannot use the lift")	
	"""
"""person = int(input("enter the total person: "))
weight_list = []
for i in range(1,person+1):
	weight = int(input("enter weight: "))
	weight_list.append(weight)
print(weight_list)

print("Lift Capacity")
max_weight = int(input("Enter Max Weight Capacity : "))
max_person_per_round = int(input("Enter Max Person Per Round : "))

master_round_list = []
round_list = []
current_round_weight = 0

for j in weight_list : 
	temp_member = len(round_list) + 1
	temp_weight = current_round_weight + j
	if temp_member <= max_person_per_round and temp_weight <= max_weight  :
		current_round_weight = temp_weight
		round_list.append(j)
	else : 
		master_round_list.append(round_list)
		round_list = []
		current_round_weight = 0
		current_round_weight = current_round_weight + j
		round_list.append(j)
	

else : 
	master_round_list.append(round_list)



print("Rounds Required : ", len(master_round_list))
print("Round Details")
for k in range(len(master_round_list)) : 
	print("Round {}. -> {}".format(k+1,master_round_list[k]))


"""

#Optimized 

person = int(input("Enter the total person: "))
weight_list = []

for i in range(person):
    weight = int(input(f"Enter weight of person {i+1}: "))
    weight_list.append(weight)

print("Weights:", weight_list)

max_weight = int(input("Enter Max Weight Capacity: "))
max_person_per_round = int(input("Enter Max Person Per Round: "))

master_round_list = []
round_list = []
current_weight = 0

for weight in weight_list:
	if wieght > max_weight:
		print("gym ja lala",weight)
    # Check if we can add this person to current round
    elif (len(round_list) < max_person_per_round and 
        current_weight + weight <= max_weight):#current wieght agar <max wieght se kam ha to appended 
        round_list.append(weight)
        current_weight += weight
    else:
        # Save current round and start new one
        if round_list:  # only append if not empty
            master_round_list.append(round_list)#max person in list according to wieght agar jada ho gaya to to vo else condition me chala jayega ...
        
        round_list = [weight]
        current_weight = weight

# Don't forget the last round
if round_list:
    master_round_list.append(round_list)

print("Rounds Required : ", len(master_round_list))
print("Round Details")
for k in range(len(master_round_list)) : 
	print("Round {}. -> {}".format(k+1,master_round_list[k]))




	