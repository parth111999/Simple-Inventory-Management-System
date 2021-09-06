import json
import time
import datetime

Name=input("Please enter your name: ")
Mob_no = int(input("Enter your mobile number "))
print(f"Hello {Name} ! Welcome to our Shopping Store. Buy Products at Discounted & Cheapest Rate !!")
        
def addInventory():
    password = int(input("Enter the password "))
    if(password == 1234):
        with open("record.json","r") as fr:
            r = fr.read()
            items_dict = json.loads(r)
        prod_id = str(input("Enter product id: "))
        prod_name = str(input("Enter name:"))
        prod_pr = int(input("Enter price: "))
        prod_qn = int(input("Enter quantity: "))
        prod_exp = str(input("Enter Expiry Date: "))
        prod_type = str(input("Enter Product Type: "))
        items_dict[prod_id] = {'name': prod_name, 'pr': prod_pr, 'qn': prod_qn, 'exp': prod_exp, 'type': prod_type}
        js = json.dumps(items_dict)
        with open("record.json","w") as fw:
           fw.write(js)
    print(f"Product ID - {prod_id} : {prod_name} added to stock records !!")

def itemPurchase():
    with open ("record.json","r") as f:
        r = f.read()
        items_dict = json.loads(r)
    print("Loading items ... Please Wait !!!")
    time.sleep(2)

    # Print All Items in Stock
    print(f"Items Available at Our Stores are: {items_dict.keys()}")
    bill = 0
    i = 0
    num_items = 100
    ls_items = []
    ls_itemname = []
    ls_quan = []
    ls_price = []
    ls_total = []
    while(num_items > 0):
        print("========================================================================================")
        itemid = input("Enter one Product-ID that you wish to Purchase: ")
        quan = int(input("Enter the quantity of Product: "))
        ls_prod = items_dict[itemid]['name']
        ls_pr = items_dict[itemid]['pr']
        ls_type = items_dict[itemid]['type']
        ls_expiry = items_dict[itemid]['exp']
        ls_bill = items_dict[itemid]['pr'] * quan
        print("Product: ", ls_prod)
        print("Price: ", ls_pr)
        print("Type: ", ls_type)
        print("Expiry Date: ", ls_expiry)
        print("Billing Amount: ", ls_bill)
        if(itemid in items_dict):
            bill = bill + items_dict[itemid]['pr'] * quan
            ls_items.append(str(itemid))
            ls_itemname.append(str(ls_prod))
            ls_quan.append(str(quan))
            ls_price.append(str(ls_pr))
            ls_total.append(str(ls_bill))
            num_items += 1
            i += 1
            items_dict[itemid]["qn"] = items_dict[itemid]["qn"] - quan
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
    print(f"Customer Name : {Name}            Time & Date of Shopping : {time.ctime()}")
    print(f"Following are the Items that you have purchased {ls_itemname} and the count of items is {i} ")
    print("========================================================================================")
    time.sleep(2)
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
        file=open(invoice+" ("+Name+").txt","w")     
        file.write("=============================================================\n")
        file.write(" SHOPPING CART                                     INVOICE\n")
        file.write(f" Invoice No: {invoice}      Date: {d}     Time: {e}\n")
        file.write(f" Name of Customer: {str(Name)}     Mobile No - {Mob_no}\n") 
        file.write("=============================================================\n")
        file.write(" PARTICULAR           QUANTITY         PRICE        TOTAL\n")                     
        file.write("-------------------------------------------------------------\n")
        for u in range(len(ls_items)):
            i = ls_itemname[u]
            j = ls_quan[u]
            p = ls_price[u]
            l = ls_total[u]
            file.write(f"   {i}                  {j}              {p}          {l}    \n")
        file.write("-------------------------------------------------------------\n")
        file.write(f"\n		     	Your Billing amount: {str(bill)}")
        file.write("\n-------------------------------------------------------------")
        file.write(f"\n   		      Your {str(disc)}% discounted amount is: {str(discount)}")
        file.write("\n-------------------------------------------------------------")
        file.write(f"\n		    	 Your payable amount is: {str(total)}")
        file.write("\n-------------------------------------------------------------")
        file.write(f"\n	          Thank You {Name} for shopping.\n	                	See you again!")
        file.write("\n=============================================================")
        file.close()
        time.sleep(2)
    else:
        print("Thanks For Saving Paper !!")
    
    # Reducing Stock Quantity as Per Purchase
    
    js = json.dumps(items_dict)
    with open("record.json" , "w") as f:
        f.write(js)

    # Sales Generation
    t = time.ctime()
    for i in range(len(ls_items)):
        sale = {"Name": Name , "Mobile_number": Mob_no, "Time": t, "Prices of each product": ls_price ,"Name_prod of each": ls_itemname,"Quantity of each product": ls_quan, "Total Bill amount": str(bill)}
        sales = json.dumps(sale)
    fd = open("Sales.json",'a')
    fd.write(sales + "\n")
    fd.close()

print("========================================================================================")
print(f"======================= WELCOME {Name} TO THE SHOPPING CART ==========================")
print("=========================== Do Visit us At @shopcart.com ===============================")
print("========================================================================================")

print("Please Choose from the Below Option : ")

print("1. Item Purchase : ")
print("2. Add Items to The Inventory : ")

choice = int(input("Enter Your Choice Here : "))
print("OK .. Wait For The Next Step ... ")
time.sleep(2)

if (choice == 1):
    itemPurchase()
elif (choice == 2):
    addInventory()

print("========================================================================================")
print("======================= THANK YOU FOR SHOPPING WITH US =================================")
print("=============================== Do Visit Again =========================================")
print("========================================================================================")