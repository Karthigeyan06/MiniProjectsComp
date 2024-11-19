print("ROYAL FRUITS SHOP")
items=[]
items_name=["Apple", "Banana", "Mango", "Pappaya", "Water melon"]
for i in range(len(items_name)):
    print("Enter the price for {}:".format(items_name[i]))
    p=int(input())
    items.append(p)
for j in range(len(items)):
    print("Price of {} = Rs.{}/-".format(items_name[j],items[j]))
print("No of items={}".format(len(items_name)))
print("Total amount= Rs.{}/-".format(sum(items)))
