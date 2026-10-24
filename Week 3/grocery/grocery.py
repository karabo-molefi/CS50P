item_list = []
while True:
    try:
        items = input().upper()
        item_list.append(items)
    except EOFError:
        break
print()
import numpy as np

values, keys = np.unique(item_list, return_counts=True)

item_dict = {values[i]: keys[i] for i in range(len(values))}

for item in item_dict:
    print(item_dict[item], item)

exit()
item_list = []

while True:
    try:
        items = input().upper()
        item_list.append(items)
    except EOFError:
        break

import numpy as np

values, counts = np.unique(item_list, return_counts=True)

grocery_dict = {}

for key in counts:
    for value in values:
        grocery_dict[key] = value
        values.remove(value)
        break

for i in grocery_dict:
    print(grocery_dict, grocery_dict[i])



grocery_dict[items] = grocery_dict.get(items, 0) + 1

grocery_list = list(grocery_dict)
grocery_list.sort()

# count the number of unique and identical items in list
for items in grocery_list:
    print(items)