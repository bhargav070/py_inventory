import json
from tabulate import tabulate

def Admin():
	print("========\
	Welcome to the Admin Inventory Management System \
	==============")
	while (1):
		print("1)Display DataBase/All Products with there details")
		print("2)Display Specific Product with its details")
		print("3)Insert Data Into DataBase")
		print("4)Update Product in Database")
		print("5)Delete Product in DataBase")
		print("6)Display User Purchase Reports")
		print("0)Exit")
		n = int(input("Enter Your Choice :- "))
		print()
		if (n == 1):
		    display_data()
		elif (n == 2):
			display_specific_data(input("Enter name of item to see its details : "))
		elif (n == 3):
		 	add_new()
		elif (n == 4):
		 	update_prod_data()
		elif (n == 5):
		 	delete_prod()
		# elif (n == 6):
		# 	display_reports_admin()
		elif (n == 0):
		 	break
		else:
		 	print("Invalid Choice...!!!")


def display_data():
	fd = open("data.json",'r')
	txt = fd.read()
	data = json.loads(txt)

	items = []
	for i in data:
		items.append(list(data[i].values()))

	print('\n')	
	print(tabulate(items, headers=['Name' ,'Price','Category','Quantity','Date of arrival']))
	print('\n\n')
	

def display_specific_data(id):
	file = open("data.json","r")
	data = file.read()
	value = json.loads(data)
	id_items = []
	id_items.append(list(value[id].values()))
	print('\n')
	print(tabulate(id_items, headers=['Name' ,'Price','Category','Quantity','Date of arrival']))
	print('\n\n')
	file.close()


def add_new():
	fd = open("data.json", 'r')
	txt = fd.read()
	data = json.loads(txt)
	fd.close()
	print("Enter New Product ID :- ")
	id = input()

	if id not in data.keys():
		name =input("Enter Product Name :- ")
		price = input("Enter Price of Product(price for product quantity as 1) :- ")
		category = input("Enter Category of Product :- ")
		quantity = input("Enter Quantity of Product :- ")
		date =input("Enter The Date on Which Product is Added in Inventory :- ")

		data[id] = {'name': name, 'price': price,'category': category, 'quantity': quantity, 'date': date}
		
		print("Product ID "+str(id)+" Added Successfully...!!!\n")
	else:
		print("The Product ID you Have Entered is Already Present in DataBase Please Check...!!!\n")
	js = json.dumps(data)
	fd = open("data.json", 'w')
	fd.write(js)
	fd.close()

#deleting particular product from inventory
def delete_prod():
	fd = open("data.json", 'r')
	txt = fd.read()
	data = json.loads(txt)
	fd.close()
	temp =input("Enter The Product ID of The Product Which You Want To Delete :- ")
	
	if temp in data.keys():
		data.pop(temp) # here we are removing that particular data
		print("Product ID "+str(temp)+" Deleted Successfully...!!!\n")
	else:
		print("Invalid Product ID...!!!\n")
	js = json.dumps(data)
	fd = open("data.json", 'w')
	fd.write(js)
	fd.close()
	
def update_prod_data():
	fd = open("data.json", 'r')
	txt = fd.read()
	data = json.loads(txt)
	fd.close()
	temp = input("Enter The Product ID of The Product Which You Want To Update :- ")
	
	if temp in data.keys():
		q = int(input("Want to update whole product data press '0' else '1' for specific data :- "))
		
		if (q == 0):
			name = input("Enter Product Name :- ")
			price = input("Enter Price of Product(price for	product quantity as 1) :- ")
			category= input("Enter Category of Product :- ")
			quantity = input("Enter Quantity of Product :- ")	
			date = input("Enter The Date on Which Product is Added in Inventory :- ")
	
			data[temp] = {'name': name, 'price': price,'category': category, 'quantity': quantity,'date': date}
			
			print("Product ID "+str(temp)+" Updated Successfully...!!!\n")
			
		elif(q == 1):
			p = input("Enter Which Attribute of Product You want to Update :- ")
			
			if p in data[temp].keys():
				print("Enter "+str(p)+" of Product :- ")
				u = input()
				data[temp][p] = u
				print("Product ID "+str(temp)+"'s attribute " +str(p)+" is Updated Successfully...!!!\n")
			else:
				print("Invalid Product Attribute...!!!\n")
		else:
			print("Invalid Choice...!!!\n")
	else:
		print("Invalid Product ID...!!!\n")
	js = json.dumps(data)
	fd = open("data.json", 'w')
	fd.write(js)
	fd.close()

