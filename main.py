import time

price_dict = {"Rice":50, "Dal":70, "Tea":20, "Wheat":30, "Sugar":40,
               "Groundnut":50, "Chanadal" :60, "Poha":35,"Rava":25,"Sabudana":90}

a_name=input("Please enter your name: ")
print(f"Hello {a_name} ! Welcome to our Shopping Store. Buy Products at Discounted & Cheapest Rate !!")

def addInventory():
    pass
    
def complain():
    pass

def others():
    pass

def itemPurchase():
    print("Loading items ... Please Wait !!!")
    time.sleep(3)
    print(f"Items Available at Our Stores are {price_dict} ")
    bill = 0
    i = 0
    num_items = 100
    ls_items = []
    while(num_items > 0):
        print("========================================================================================")
        item = input("Enter one item that you wish to purchase: ")
        x = item.capitalize()
        quan = int(input("Alsoo Enter the quantity in kgs: "))
        if(x in price_dict):
            bill = bill + quan*price_dict[x]
            ls_items.append(x)
            num_items += 1
            i += 1
        else:
            print("========================================================================================")
            print("We Dont Have This Item as of Now. ")
            print("========================================================================================")
        wish = input("Do You Wish To enter another item y/n : ")
        if(wish == "y"):
            continue
        else:
            break
    if (bill <= 500):
        disc = 5.0
        discount = (disc*bill)/100
        total=float(bill-discount)
    elif (bill >= 500):
        disc = 10.0
        discount = (disc*bill)/100
        total=float(bill-discount)
    time.sleep(3)

    print("You Can Sit Back & Relax Until We Generate Your Invoice.")    
    print("========================================================================================") 
    print(f"Customer Name : {a_name}            Time & Date of Shopping : {time.ctime()}")
    print(f"Following are the Items that you have purchased {ls_items} and the count of items is {i} ")
    print("========================================================================================")
    time.sleep(3)
    print(f"           Your Bill Amount is {bill} for the items you have purchased.  ")
    print(f"        You got your expected {disc}% discount and Your Payable Amount is: {total}")
    print("======================= Pay Your Bill on Cash Counter ==================================")
    

print("========================================================================================")
print(f"======================= WELCOME {a_name} TO THE SHOPPING CART =============================")
print("=========================== Do Visit us At @shopcart.com ===============================")
print("========================================================================================")

print("Please Choose from the Below Option : ")

print("1. Item Purchase : ")
print("2. Add Items to The Inventory : ")
print("3. Complain : ")
print("4. Any Others : ")

choice = int(input("Enter Your Choice Here : "))
print("OK .. Wait For The Next Step ... ")
time.sleep(3)

if (choice == 1):
    itemPurchase()
elif (choice == 2):
    addInventory()
elif (choice == 3):
    choice()
elif (choice == 4):
    others()

print("========================================================================================")
print("======================= THANK YOU FOR SHOPPING WITH US =================================")
print("=============================== Do Visit Again =========================================")
print("========================================================================================")