import json
import admin

file = open("data.json","r")
txt = file.read()
data = json.loads(txt)
file.close()

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
            
    n = int(input("Enter 1 to add more item and 0 to get bill :"))
    if n == 0:
        break
for i in range(len(ID)):
    amount = int(data[ID[i]]['price'] * buy_q[i])
    items.append(list([ID[i] , buy_q[i] , amount]))

print(ID)
print(buy_q)
print(items)

fd = open('bill.txt')
txt = fd.readlines()

for i in range(len(txt)):
    print(txt[i])

