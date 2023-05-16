waiting_list = ["Sadiya", "Latifa", "Abdul Rahman"]
#Note: list is mutable and method itself (here sort()) returns nothing. It already is sorted here and enough
waiting_list.sort()
for index, item in enumerate(waiting_list):
    row = f"{index + 1}.{item.capitalize()}"
    print(row)

'''
filenames = ['document', 'report', 'presentation']
for i, j in enumerate(filenames):
    print(f'{i}-{j.capitalize()}.txt')
'''

menu = ["pasta", "pizza", "salad"]
for index, j in enumerate[menu]:
    print(f"{index}.{j}")




