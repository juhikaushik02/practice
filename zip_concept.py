list1 = ["sohil", "ronil", "anita", "babita"]
list2 = ["98789", "7654", "1543", "8976"]

dict1 = {1: 'juhi', 2: 'kaushik', 3: 'abc'}
dict2 = {1: 123, 2: 456, 3: 789}
dict3 = {123: 'juhi', 456: 'kaushik', 789: 'abc'}

for (k1, v1), (k2, v2) in zip(dict1.items(), dict2.items()):
    print(f' {v2} : {v1}')
    dict3[v2] = v1

# print(dict3)

# for index in range(len(list1)):
#     if list1[index].lower() == 'anita':
#         list2[index] = '3145'
# print(list2)

for list1_item, list2_item in zip(list1, list2):
    print(list1_item + " : " + list2_item)

dict4 = dict(zip(list2, list1))
