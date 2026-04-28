

"""print("MENU:")
print("1. Pizza        - ₹200")
print("2. Burger       - ₹120")
print("3. Pasta        - ₹150")
print("4. Sandwich     - ₹100")
print("5. Coffee       - ₹80")

choice = int(input("Enter item number (1-5): "))
quantity = int(input("Enter quantity: "))

if choice == 1:
    item = "Pizza"
    price = 200
elif choice == 2:
    item = "Burger"
    price = 120
elif choice == 3:
    item = "Pasta"
    price = 150
elif choice == 4:
    item = "Sandwich"
    price = 100
elif choice == 5:
    item = "Coffee"
    price = 80
else:
    print("Invalid choice!")
    

amount = price * quantity

gst = amount * 0.05

final_amount = amount + gst

print("BILL")
print("Item:", item)
print("Price per item: RS", price)
print("Quantity:", quantity)
print("Amount: Rs", amount)
print("GST (5%): RS", round(gst))
print("total bill is: RS", (final_amount))
"""
menu = ["1.Veg Thali: ₹150","2.Paneer Butter Masala: ₹180","3.Dal Tadka: ₹110",
"4.Mixed Veg Curry: ₹130","5.Jeera Rice: ₹90","6.Tawa Roti: ₹10","7.Butter Naan: ₹30",
"8.Veg Fried Rice: ₹140","9.Masala Papad: ₹20","10.Lassi: ₹50"]
menu_1 = ["Veg Thali","Paneer Butter Masala","Dal Tadka",
"Mixed Veg Curry","Jeera Rice","Tawa Roti","Butter Naan",
".Veg Fried Rice","Masala Papad","Lassi"]
price = (150,180,110,130,90,10,30,140,20,50)
for i in range(len(menu)):
    print(menu[i])
list_1 = []
list_2 = ["item name"]
list_3 = ["quantity"]
list_4 = ["rate"]
list_5 = ["amount"]
order = int(input("tell me how many items you have selected: "))
for i in range(order) :
    order_No = int(input("tell me what is your order but give that in Number: "))
    name = menu_1[order_No-1]
    list_2.append(name)
    quantity = int(input("in how much quantity: "))
    list_3.append(quantity)
    rate = price[order_No-1]
    list_4.append(rate)
    item_rate = rate*quantity
    list_1.append(item_rate)
    list_5.append(item_rate)
    total = sum(list_1)
for i in range(len(list_2)) :
    print(list_2[i],list_3[i],list_4[i],list_5[i])
print("your total without tax is ", total)
total_bill = (5/100)*total
print("your tax amount on the bill is  ", total_bill)
total_bill+=total
total_bill = round(total_bill)
print("your final bill amount is {}".format(total_bill))





