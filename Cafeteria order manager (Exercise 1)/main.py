
from array import array

n = int(input("Numbers of orders: "))
quantities = []
for i in range(n):
    h=int(input(f"Enter Quantity of your order {i+1} in Kgs: "))
    quantities.append(h)

total = sum(quantities) 
average = total / n
min = min(quantities)
max = max(quantities)

print("-----The simple report-------\n")

report = f"The number of orders received are {n}.\n"
report += f" The Quantity sum of received orders are {total}.\n"
report += f" The average of ordered received:  {average}."

print(f"{report}")


threshold = int(input("Enter the threshold Value: "))
if average >threshold and max > threshold:
    print("Status: Above Standard")
else:
    print("Status: Below standard")

print("\n The orginal List." , quantities)
new_quantity = int(input("Enter the new Order quantity: "))
quantities.append(new_quantity)

print("\n The List after adding new quantity", quantities)

remover_val = int(input("\n Enter quantity order you want to remove: "))
if remover_val in quantities :
    quantities.remove(remover_val)

print("\n The List after  removing quantity", quantities)

quantities.sort()

print("\n  Sorted Quantities", quantities)

#------------------array--------------------

# Create an array for order quantities (all integers)
quantities_array = array('i', quantities)
print("\nArray version of quantities:", quantities_array)
print("Accessing first element in array:", quantities_array[0])

record = []
for i in range (n):
    record_id = int(input(f"Enter id {i+1}: "))
    record_name = input("Enter name: ")
    record_value= int(input("Enter the value: "))
    record.append({"id": record_id, "name": record_name,"value": record_value})


print("\n the Records before update: ", record , "\n")

record[0]["value"] += 90
 
print("the Records after update: ", record , "\n")
if len(record) > 1:
    del record[2]

print("the Records after Delete: ", record , "\n")

total_val = sum(x["value"] for x in record)

print("\n Final results: ", record , "\n")

print("\n Total value from records:", total_val)

