# find duplicate items in a list
items = ["apple", "banana", "orange", "banana", "mango"]

unique_items = set()

for item in items:
    if item in unique_items:
        print("Duplicate Item:",item)
        # break
        exit()
    unique_items.add(item)

print("No Duplicate Item")