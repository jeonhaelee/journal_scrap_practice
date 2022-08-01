li1 = [1,2,3]
li2 = [4,5,6]
li3 = [7,8,9]

all_list = []

# all_list.append(li1)
# all_list.append(li2)
# all_list.append(li3)

# print(all_list)

all_list.extend(li1)
print(all_list)
all_list.extend(li2)
print(all_list)
all_list.extend(li3)
print(all_list)


dic1 = {"1" : "aaa", "2" : "bbb"}
dic2 = {"3" : "ccc", "4" : "ddd"}
dic3 = {"5" : "eee", "6" : "fff"}

dic1.update(dic2)
dic1.update(dic3)
print(dic1)

