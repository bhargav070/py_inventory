import admin
import consumer
import json


def main():
	print("========Welcome to the Inventory Management System ==============")
	while(1):
		print("1)Admin")
		print("2)Customer ")
		print("0)Exit")
		n = int(input("Enter Your Choice :- "))

		if (n == 1):
			admin.Admin()
		elif n == 2:
			consumer.user()
		elif n == 0:
		 	exit()

main()
