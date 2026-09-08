from tabulate import tabulate
import json
import admin
import os.path
import random
import time

def user():
    print("===========================Welcome To Consumer Section===============================")
    while(1):
        print("1)Display all Products")		
        print("1)Display specific Product")	
        print("3)Buy product")
        print("0)exit")
        n = int(input("Enter your choice : "))

        if n==1:
            admin.display_data()
        elif n==2:
            pr = input("Enter id of product to see its details : ")
            admin.display_specific_data(pr)

        elif n==3:
            buy_product()

        elif n==0:
            break
        else:
            print("Invalid choice !!!")	

def generate_bill(items,user_name):
    fd = open("user_data.json",'r+')
    txt = fd.read()
    user_data = json.loads(txt)

    total =0 

    transaction_id = ''.join(random.choice('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') for i in range(10))
    purchase_time = str(time.ctime())

    for i in range(len(items)):
        total += items[i][2]
        items[i].append(transaction_id)
        items[i].append(purchase_time)

    fd = open("bill.txt",'w')

    bill = []
    bill.append("/===============================Invoice=======================================/\n")
    bill.append("User Id : "+ str(user_name)+'\n')
    bill.append(tabulate(items ,headers=['Product' , 'Price' ,'Amount' ,'Transaction ID' , 'Purchase time']))
    bill.append('\n')
    bill.append("\tTotal amount : "+str(total) +'\n')
    bill.append('/=============================================================================/\n')

    for i in range(len(bill)):
        fd.write(bill[i])
    
    temp = {}
    temp[user_name] = bill
    user_data[user_name] = json.dumps(temp)
    return transaction_id

#functiona for buying product
def buy_product():
    user_data = {}
    
    fd = open("user_data.json",'r')
    txt = fd.read()
    user_data = json.loads(txt)
    fd.close()

    fd = open('data.json','r')
    txt = fd.read()
    data = json.loads(txt)
    fd.close()
    
    new_or_old = int(input("Enter 1)Old Cutomer  2)New customer :"))

    if new_or_old==1:
        n = 1
        while 1:
            user_name = input("Enter your User name : ")
            if user_name in user_data:
                break
            else:
                n2 = int(input("Invalid user name ,If want a new account enter 1\n"))
                if n2 == 1:
                    new_or_old = 2
                    break
    else:
        print("Creating a new user account .....")
        u_id = input("Enter new user name : ")
        
    items = []
    ID =[]
    buy_q =[]
    while(1):

        x = (input("Enter ID of product you want to buy :"))
        admin.display_specific_data(x)
        ID.append(x)
        y = (int(input("Enter quantity: ")))
        if y > data[x]['quantity']:
            print("Maximum amount selected ! :" + str(data[x]['quantity']))
            y = data[x]['quantity']
        buy_q.append(y)

        #deduct purchased amount from data
        data[x]['quantity'] -= y
                
        n = int(input("Enter 1 to add more item and 0 to get bill :"))
        if n==0:
            break
               
    for i in range(len(ID)):
        amount = int(data[ID[i]]['price'] * buy_q[i])
        items.append([data[ID[i]]['name'] , buy_q[i] , amount])
    
    #dumping updated data after puchase in json file
    fd = open("data.json","w")
    txt = json.dumps(data)
    fd.write(txt)
    fd.close()
            
    #calling generate bill 
    t_id = generate_bill(items,u_id)

    #creating user data as {user id : transaction id} and dumping it in user data file
    txt = json.dumps(user_data)
    fd = open("user_data.json",'a')
    fd.write(txt)
    fd.close()
    

    

