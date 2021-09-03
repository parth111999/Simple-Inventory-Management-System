import json
import time
import datetime

a_name=input("Please enter your name: ")
print(f"Hello {a_name} ! Welcome to our Shopping Store. Buy Products at Discounted & Cheapest Rate !!")

def addInventory():
    pass
    
def complain():
    pass

def others():
    pass

def itemPurchase():
    with open ("record.json","r") as f:
        r = f.read()
        price_dict = json.loads(r)
    print("Loading items ... Please Wait !!!")
    time.sleep(3)
    print(f"Items Available at Our Stores are {price_dict} ")
    bill = 0
    i = 0
    num_items = 100
    ls_items = []
    while(num_items > 0):
        print("========================================================================================")
        item = input("Enter one item that you wish to Purchase: ")
        x = item.capitalize()
        quan = int(input("Enter the quantity of Product: "))
        print("Product: ", price_dict[x]['name'])
        print("Price: ", price_dict[x]['pr'])
        print("Billing Amount: ", price_dict[x]['pr'] * quan)
        if(x in price_dict):
            bill = bill + price_dict[x]['pr'] * quan
            ls_items.append(x)
            num_items += 1
            i += 1
            price_dict[x]["qn"] = price_dict[x]["qn"] - quan
        else:
            print("========================================================================================")
            print("We Dont Have This Item as of Now. ")
            print("========================================================================================")
        wish = input("Do You Wish To enter another item y/n : ")
        if(wish == "y"):
            continue
        else:
            break


    # Discount Calculations
    if (bill <= 500):
        disc = 5.0
        discount = (disc*bill)/100
        total=float(bill-discount)
    elif (bill >= 500):
        disc = 10.0
        discount = (disc*bill)/100
        total=float(bill-discount)
    
    # Bill Generation
    print("You Can Sit Back & Relax Until We Calculate Your Bill.")    
    print("========================================================================================") 
    print(f"Customer Name : {a_name}            Time & Date of Shopping : {time.ctime()}")
    print(f"Following are the Items that you have purchased {ls_items} and the count of items is {i} ")
    print("========================================================================================")
    time.sleep(3)
    print(f"           Your Bill Amount is {bill} for the items you have purchased.  ")
    print(f"        You got your expected {disc}% discount and Your Payable Amount is: {total}")
    print("======================= Pay Your Bill on Cash Counter ==================================")
    
    # Invoice Generation
    wishinvoice = input("Do You Wish To print an Invoice Copy y/n : ")
    if(wishinvoice == "y"):
        # Printing Date & Time of Invoice Generation 
        dt=str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day)+"-"+str(datetime.datetime.now().hour)+"-"+str(datetime.datetime.now().minute)+"-"+str(datetime.datetime.now().second)
        invoice=str(dt)    #unique invoice
        t=str(datetime.datetime.now().year)+"-"+str(datetime.datetime.now().month)+"-"+str(datetime.datetime.now().day) #date
        d=str(t)    #date
        u=str(datetime.datetime.now().hour)+":"+str(datetime.datetime.now().minute)+":"+str(datetime.datetime.now().second) #time
        e=str(u)    #time
        # File I/O
        file=open(invoice+" ("+a_name+").txt","w")     
        file.write("=============================================================\n")
        file.write(" SHOPPING CART                                     INVOICE\n")
        file.write(f" Invoice No: {invoice}      Date: {d}     Time: {e}\n")
        file.write(f" Name of Customer: {str(a_name)}\n")
        file.write("=============================================================\n")
        file.write(" PARTICULAR           QUANTITY           PRICE        TOTAL\n")                     
        file.write("-------------------------------------------------------------\n")
        file.write(f"{price_dict[x]['name']}                 {quan}                 {price_dict[x]['pr']}           {quan*price_dict[x]['pr']}\n")
        file.write("-------------------------------------------------------------\n")
        file.write(f"\n		     	Your Billing amount: {str(bill)}")
        file.write("\n-------------------------------------------------------------")
        file.write(f"\n   		      Your {str(disc)}% discounted amount is: {str(discount)}")
        file.write("\n-------------------------------------------------------------")
        file.write(f"\n		    	 Your payable amount is: {str(total)}")
        file.write("\n-------------------------------------------------------------")
        file.write(f"\n	          Thank You {a_name} for shopping.\n	                	See you again!")
        file.write("\n=============================================================")
        file.close()
        time.sleep(3)
    else:
        print("Thanks For Saving Paper !!")
    
    # Reducing Stock Quantity as Per Purchase
    
    js = json.dumps(price_dict)
    with open("record.json" , "w") as f:
        f.write(js)

    

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