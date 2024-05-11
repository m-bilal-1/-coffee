dict_menu={
    "pizza":130,
    "coffee":120,
    "bisciuts":40,
    "juice":120,
    "shake":120,
    "cake":100
}


print("WELCOME TO BILAL HOUSE OF COFFEE RESTURANT")
print("------------------------------------------")
print("------------------------------------------")
print("===============Menu====================")

print("============Pizza : 130/-=================")
print("============coffee : 130/-================")
print("============biscuits: 130/-================")
print("============juice : 130/-==================")
print("============shakes : 130/-=================")
print("=========== cake : 130/-===================\n\n")
price=0
invoice=[]
while True:
    user=input("Enter your order: ")
    if user in dict_menu:
        print(f"The item {user} is added on order\n\n")
        price+=dict_menu[user]
        invoice.append((user,dict_menu[user]))
    elif user == "no":
        print("Thank you\n\n")
        print("------------------")
        print("------------------")
        for item,price in invoice:

            print(f"{item}:{price}\-")
        print("------------------")
        print("------------------")
        print(f"The total bill is {price}")
    else:
        print("Enter valid thing")

