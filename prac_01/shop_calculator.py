
while True:
    num_items = int(input("Number of items: "))
    if num_items >= 0:
        break
    else:
        print("Invalid number of items! Please enter a non-negative number.")

total_price = 0

for i in range(num_items):
    price = float(input("Price of item: "))
    total_price += price

print("Total price for {} items is ${:.2f}".format(num_items, total_price))
